---
title: NCTS Phase 5 Technical Interface Specification
weight: 1
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---

# NCTS Phase 5 Technical Interface Specification

Version 0.0.1a issued April 2022
***


## Introduction

The New Computerised Transit System (NCTS) is a European-wide system, based upon electronic declaration and processing, designed to provide better management and control of Union and Common Transit. It involves all countries comprising the EU Member States and all Common Transit Convention contracting countries. 

The NCTS connects each country through a central domain in Brussels, to all of the other countries, linking the European customs offices.

The main objectives of the NCTS are:

- to increase the efficiency and effectiveness of transit procedures
- to improve both the prevention and detection of fraud
- to accelerate transactions carried out under a transit procedure and to offer security for them

In order to use the NCTS, traders need the facility to send and receive electronic messages to and from the UK - NCTS. Connected traders receive electronic responses advising of key decisions during both departure and destination, such as:

- acceptance of declaration
- release of goods
- notification of discharge of liability 

Traders cannot interface directly with the NCTS to input or amend data or to access records and reference data, but simply exchange defined structured messages with the system. 

In certain circumstances, where Simplified NCTS Procedures are used by Authorised Consignors/Consignees, processing and release will be automatic and allow, depending upon the conditions of authorisation, for 'out of hours' clearance. This will allow for selective, risk-based controls, and for the processing of declarations and the release of goods to become largely automatic.

### Scope

This document gives an overview of the processes involved in the exchange of NCTS messages with traders and defines the messages associated with NCTS, in particular:

- the trader’s declaration for Transit and associated Customs response
- control and release of the movement 
- the trader’s notification of arrival and associated Customs response
- control and release of the goods

These messages are developed following the Functional Transit System Specification (FTSS) and Design Documentation for National Transit Application (DDNTA) documents distributed by the EU Commission to National Administrations.

### NCTS Reference Data

NCTS has been developed using the Minimal Common Core (MCC) software package provided by the EU Commission.

NCTS holds two types of reference data:

- common reference data which is held on a central system known as Common Services Reference Data (CS/RD2) which is applicable to all contracting parties NCTS systems
- national reference data which applies locally to individual countries systems

#### CS/RD2

Reference data within CS/RD2 is made of code lists. Each code list provides data which is used for validation against specific fields within declarations submitted by users and intra NCTS system message exchange. The latest CS/RD2 data is released overnight on a daily basis. The most volatile code list contained within CS/RD2 is CL 141 Customs Offices, which holds details of all valid Customs Offices for all Common Transit Convention countries including the transit functions available per office i.e. Office of Departure (DEP), Office of Destination (DES) and Office of Transit (TRA).

It is essential that the software solution you develop retrieves these updates on a daily basis to ensure any validation you code in is synchronised with UK NCTS to prevent unnecessary rejections.

#### National Reference Data

This is administered by each National Administration on its own behalf. It is used for validation against country specific data such as guarantees, and authorised location codes used by authorised consignors and consignees for simplified procedures.

### The UK's approach to EU Exit

As a result of the UK leaving the EU and becoming a contracting party to the Common Transit in its own right, the benefits of transit usage have been retained for UK businesses.

Transit movements to and from Great Britain (GB) are no longer under Union Transit but under Common Transit. However, due to the needs of the Northern Ireland Protocol,  transit movements are treated as beginning or ending under Union Transit.

This means that while the declaration data sets for Union and Common Transit are identical, validation carried out against each data field is sometimes conditional. Some of these conditions are based upon the location of transit offices involved in the movement being either in or outside the EU. For example, some information that may be optional under Union Transit will be mandatory under Common Transit or the other way round, according to the conditions and rules defined by the Common Transit Convention. The condition and rule number applicable to each data field is shown in the message tables for Transit Declarations and Arrival Notifications. Full details of the conditions and rules are shown in embedded links.

The condition that has the most regular impact on UK NCTS users is C030 which requires an Office of Transit to be declared where the office of departure is a common transit country i.e. outside the EU. C030 also prevents the usage of TIR within NCTS for Common Transit countries therefore a TIR type movement cannot start, end or traverse GB mainland and crown dependencies using NCTS.

Because Northern Ireland needs to operate transit in alignment with the UCC i.e. Union Transit, we have introduced a separate NCTS service specifically for Northern Ireland to make sure the Common Transit Convention conditions and its rules are applied correctly. GB and NI NCTS systems are two separate instances of the same common core operating independently. The only difference between them is the identifying country code and mode of operation – GB applies data validation in alignment with Common Transit rules, NI applies validation in alignment with Union Transit rules.

### Dual NCTS implementation overview – changes from 1 January 2021

#### Great Britain NCTS

The Great Britain NCTS service will only accept departure and arrival declarations for Transit offices located in mainland Great Britain and Crown Dependencies (Channel Islands and Isle of Man).

It will not accept the departure and arrival declarations for Transit offices located in Northern Ireland.

#### Northern Ireland NCTS

The Northern Ireland NCTS service will operate in Union Transit mode. It will only accept departure and arrival declarations in respect of Transit offices located in Northern Ireland.

It will not accept departure and arrival declarations for Transit offices located in mainland Great Britain and Crown Dependencies (Channel Islands and Isle of Man).

#### The country codes for the dual system

All Common Transit Convention members and their mode of transit operation (such as Union or Common) are identified through CS/RD2 data shared between all members’ NCTS systems. This is essential to make sure declaration data meets the applicable conditions and rules of the countries involved in any given transit movement.

As a result of this, the Great Britain and Northern Ireland NCTS services will operate with separate country codes:

- Great Britain NCTS will keep its country prefix GB
- Northern Ireland NCTS will use the prefix XI

NCTS needs region-specific reference data to include the applicable country code. This includes reference data such as customs office codes, guarantee reference numbers and Economic Operator Registration and Identification (EORI) (also known as Trader Identification Number).

Customs offices located in mainland Great Britain, pre-existing EORIs and related guarantees keep their GB prefix for the Great Britain NCTS service.

Customs offices located in Northern Ireland, new Northern Ireland specific EORIs and related guarantees will all have the prefix XI (for example, the office code for Belfast Entry Process Unit will change from GB000142 to XI000142).

Additionally, existing authorised locations used by authorised consignors and consignees that are located in Northern Ireland are migrated from the GB to XI NCTS system.

Because authorised location codes are linked to the authorised consignor/nees EORI, and because EORIs are linked to the procedure holders guarantee, the software you develop should allow both the use of GB EORIs and their associated GB guarantee as well as XI EORIS and their associated XI guarantee.

### No access to GB and XI NCTS via legacy channels

Traders may no longer exchange messages with both NCTS systems via the following legacy channels:

- By email containing EDIFACT format message
- By XML channel whereby XML is a wrapper for an EDIFACT format message

### New XML digital API

We have released a CTC trader API channel that allows 3rd party software to send and receive arrival and departure notifications using XML language for the message payload. The EDIFACT email and XML channels have become legacy and their usage has been phased out. The CTC trader API has provide full GB and NI integration since the end of March 2021 and provides a single end point for both GB and NI declarations.

### Liability Amount for Guarantees

Guarantee Management processing in NCTS requires that a liability amount is recorded against each guarantee in a declaration.

Departure declarations submitted by users (IE015) can only provide guarantee liability amounts in respect of guarantee types 0,1,2,4 and 9. For all other guarantee types, Border Force will enter the liability amount into NCTS manually prior to releasing the movement.

The previous automated default liability insertion for guarantees has been removed. Departure declarations must now include an accurate guarantee reference amount for guarantee types 0, 1, 2, 4 and 9 in both Great Britain and Northern Ireland NCTS systems.

In exceptional circumstances, where a declarant is unable to determine the guarantee reference amount, the Common Transit Convention allows the amount to be fixed at 10,000 euros for each transit operation.

For guarantee types 0, 1, 2, 4 and 9, where no reference amount is contained within the transit declaration, the system will automatically insert 10,000 euros as the guarantee liability amount.

This will apply in all circumstances except for national transit movements, for example, Great Britain to Great Britain. National transit is not supported by the Common Transit Convention however, UK national legislation allows its usage as a trade facilitation.

The above behaviour has been implemented in the trader test environment.

The EU Commission has provided a facility for traders to input a maximum of 9 occurrences, per declaration, of liability amount into the ‘Special Mentions’ field, of the IE015 message.

NCTS 4.0 can read guarantee liability records in the ‘Special Mentions’ data group whenever a declaration (IE015) is submitted.

If all the guarantees are valid, and the declaration is a simplified one, then the declaration will be automatically released.

In the event of a normal procedure declaration, then the customs officer will have to confirm (or amend) the liability amounts prior to release.

This use of ‘Special Mentions’ can be used for both Simplified and Normal procedures and for guarantee types 0, 1, 2, 4 and 9.

This ‘liability amount’ use of Special Mentions will occur in the first 9 occurrences of the first occurrence of Goods Item.

The ‘Special Mentions’ fields will be used as follows:

- ‘Additional Information Coded’ (an..3) will contain the 3 characters “CAL”
- ‘Additional Information’ (an..70) will contain:
    - ‘Calculated Liability’ (n..15,2) – liability amount in pounds sterling
    - ‘Currency Code’ (an..3) – currency of the liability amount i.e. “GBP”
    - ‘GRN’ (an..24) – 17 character GRN

The ‘Calculated Liability’ can contain up to 2 decimal places. If decimal places are used, they should be separated from the significant figures by a decimal point e.g. 362.48.

The ‘liability amount’ information is entered in the first 9 occurrences, starting at occurrence 1, of the ‘Special Mentions’ fields, in the first occurrence of ‘Goods Item’. Any use of the ‘Special Mentions’ field not containing ‘liability amount’ information, in the first occurrence of ‘Goods Item’, should occur **after** any ‘liability amount’ information e.g. if the ‘liability amount’ information is in occurrences 1 to 4, instances not containing liability amount information would be in occurrences 5 onwards.

The IE029 (Release for Transit) message will contain the **actual** ‘CAL’ fields, if the original IE015 that has been electronically received also contains "CAL" details, so as to inform the trader of the actual guarantee amount in comparison to the original guarantee amount that was declared on the IE015 message. 

**Note:** The ‘liability amount’ information in the Special Mentions data group (Additional information and Additional information coded) is not printed on the TAD i.e. if ‘Additional information coded’ = ‘CAL’, do not print.

Note that since 1/1/2021, guarantee type 8 ‘guarantee not required for certain public bodies’ is no longer valid within GB NCTS operating in Common Transit mode. It remains valid within XI NCTS operating in Union Transit mode.

### TAD (Transit Accompanying Document) / TSAD (Transit Security Accompanying Document)

A TSAD is printed for declarations containing safety and security data; a TAD is printed for all other declarations. TADs/TSADs generated from the IE029 Release for Transit (E_REL_TRA) message are automatically authenticated by NCTS. **TADs/TSADs must only be printed using information on the IE029 message**.

This means that the TAD/TSAD does not need to be authenticated by the Office of Departure by stamp.  The CT movement is not **legally** released from transit until the IE029 has been generated by customs and a valid TAD/TSAD subsequently printed.

**The TAD/TSAD should only be printed using data that has been validated or provided by the NCTS system. This can be achieved by printing the TAD/TSAD direct from the IE029 message or by using data from the IE029 to update a previously created and validated transit record, and then printing the TAD/TSAD.**

**Authorised Consignors who move goods before issue of the IE029 message are in breach of their approval conditions. Continued failure to observe the conditions of approval may lead to revocation of Authorised Consignor’s approval and/or civil penalty action.**

Traders using the Normal procedure will have the option either to collect the TAD/TSAD from the Office of Departure or to print the TAD/TSAD at their own premises. Approval to print the TAD/TSAD is granted by the CCTO, to whom the trader’s application must be submitted for consideration. The Trader must provide evidence of their ability to print the TAD/TSAD in the required format.

Traders authorised to use Simplified NCTS Procedures as Authorised Consignors, will be able to print the TAD/TSAD at their premises. The TAD/TSAD will be directly authenticated by the system, so Authorised Consignors will not be required to hold a 'special stamp'.

**Fallback procedure:** Authorised Consignors are obliged to hold special stamps to authenticate documents in case of system failure so they can authorise their own fallback documents. Authorised Consignors additionally require a Commission approved stamp that informs the Office of Destination that fallback has been used.

For the specifications on the printing of the paper TAD, see Guidelines for printing a TAD contained in Part IV, Chapter 2, Annexes 8.1 and 8.2 of the European Commission’s [Transit Manual](http://ec.europa.eu/taxation_customs/resources/documents/customs/procedural_aspects/transit/common_community/transit_manual_consolidation_en.pdf).

For the specifications on the printing of the paper TSAD, see Guidelines For Print Out of TSAD, Printing Guidelines for TSAD and TSAD and LoI.

The IE029 will specify the number of copies required. If a return copy is required, i.e. HEADER.NCTS return copy is set, then two copies of the TAD/TSAD will be required; if not, only one needs to be printed. The return copy is required when the Office of Destination (OoDest) is not using the NCTS yet.

The ‘liability amount’ information in the Special Mentions data group (Additional information and Additional information coded) is not printed on the TAD/TSAD i.e. if ‘Additional information coded’ = ‘CAL’, do not print.

If a declaration contains only one goods item, all the information for the movement is printed on the TAD. If the declaration contains more than one goods item, all the goods items are printed on the LoI (List of Items). However, if the declaration contains safety and security data, the goods item information (even if there is only one goods item) is always printed on the TSAD LoI.

The printer and print driver, used for printing the TAD/TSAD, must be capable of printing a bar code of standard ISO code 128 set B (but not EAN128). 

The font type is BC C128 Narrow (True Type) version 2.0.

### Logical Structure of the IE messages

The messages are organised into data groups that contain data items. The data items are grouped together in such a way that they build up coherent logical blocks within the scope of each message.

The messages show:

- the characteristics of the data groups belonging to the message: sequence, number of repetitions, a status value to indicate if the data group is mandatory (R: Required), optional (O: Optional) or conditional (D: Dependent)
- the characteristics of the data items belonging to a data group: sequence, number of repetitions, type, length and a value to indicate if a data item is mandatory (R: Required), optional (O: Optional) or conditional (D: Dependent)
- data group indentation indicates that the data group may contain not only data items but also other groups of data
- applicable NCTS Codelists; for example, CL008
- applicable rules and Conditions; for example, C030

**Note:** all numeric values must be greater than zero unless R021 applies.

### Important phase 5 terms

The following terms are important to understand in phase 5:

- **Consignment:** The header information is provided and applies to the whole transit declaration (up to 1 Consignment level per declaration).

- **House Consignment:** The lowest transport information is provided, and this applies to all its Consignment Items (each Consignment can contain up to 99 House Consignments).

    The House Consignment level covers information relating to all goods that are subject to the same house transport contract. A house transport contract is a transport contract with a freight forwarder, non-vessel or aircraft operating common carrier or his agent or a postal operator. Where several house transport contracts exist, the information provided in customs declarations, notifications and proof of the customs status as Union Goods should relate to the lowest level of contracts. This is usually the contract concluded by a freight forwarder and the shipper.

    The new House Consignment level is introduced to give more flexibility to the Economic Operators, allowing them to lodge one declaration with several Consignors/Consignees.

- **Consignment Item:** The items information is provided (each House Consignment can contain up to 999 Consignment Items).

## Pre-lodgement message flows

### Transit presentation notification valid 

**Applicable procedures:** normal and simplified.

<img src="figures/trans_pres_notif_valid.svg" alt="Pre-lodgement message flow with presentation of a valid notification. Flow is described in this section." />

<a href="figures/trans_pres_notif_valid.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the Office of Departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The Office of Departure validates this message successfully and sends the ‘Positive Acknowledge’ E_POS_ACK (IE928) message to the Holder of the Transit Procedure to acknowledge receipt of the transit declaration.
1. Following the result of the Risk Analysis engine, the Office of Departure may select the pre-lodged declaration for potential control of the goods prior to their presentation. In such a case, the Office of Departure notifies the Holder of the Transit Procedure (provided that they are an AEO) about the intention to potentially control the goods, via the ‘Control Decision Notification’ E_CTR_DEC (IE060) message (having the data element TRANSIT OPERATION-Notification type equal to ‘2-Intention to Control’).
1. The Office of Departure receives a valid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message from the Holder of the Transit Procedure.
1. The MRN is communicated to the Holder of the Transit Procedure with message ‘MRN Allocated’ E_MRN_ALL (IE028).
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.



### Transit presentation not valid 

**Applicable procedures:** normal and simplified.

<img src="figures/trans_pres_notif_not_valid.svg" alt="Pre-lodgement message flow with presentation of a non-valid notification. Flow is described in this section." />

<a href="figures/trans_pres_notif_not_valid.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the Office of Departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The Office of Departure validates this message successfully and sends the ‘Positive Acknowledge’ E_POS_ACK (IE928) message to the Holder of the Transit Procedure to acknowledge receipt of the transit declaration.
1. The Office of Departure receives an invalid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message from the Holder of the Transit Procedure.
1. The Office of Departure rejects the E_PRE_NOT (IE170) message by notifying the Holder of the Transit Procedure with the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message.
1. If the time limit expires without the Holder of the Transit Procedure resending a valid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message, the Holder of the Transit Procedure is notified with the message ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) by the Office of Departure.
1. The transit movement ends.



### Corrections of the pre-lodgement declaration prior to presentation of the goods 

**Applicable procedures:** normal and simplified.

<img src="figures/correct_pre-lodge_dec_prior_pres_goods.svg" alt="Pre-lodgement message flow with corrections of the pre-lodgement declaration prior to presentation of the goods. Flow is described in this section." />

<a href="figures/correct_pre-lodge_dec_prior_pres_goods.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the Office of Departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The Office of Departure validates this message successfully and sends the ‘Positive Acknowledge’ E_POS_ACK (IE928) message to the Holder of the Transit Procedure to acknowledge receipt of the transit declaration.
1. The Holder of the Transit Procedure decides to correct the transit declaration and submits the ‘Declaration Amendment’ E_DEC_AMD (IE013) message.
1. The Office of Departure performs validation of the IE013 message with one of the following outcomes:
    - The Office of Departure sends the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) to the Holder of the Transit Procedure. The Holder of the Transit Procedure can then send a second ‘Declaration Amendment’ E_DEC_AMD (IE013) message for validation. (Go to step 4.)
    - The Office of Departure validates the IE013 message successfully and sends its acceptance to the Holder of the Transit Procedure with the ‘Amendment Acceptance’ E_AMD_ACC (IE004) message. (Go to step 5.)
1. Following the result of the Risk Analysis engine, the Office of Departure may select the pre-lodged declaration for potential control of the goods prior to their presentation. In such a case, the Office of Departure notifies the Holder of the Transit Procedure (provided that they are an AEO) about the intention to potentially control the goods, via the ‘Control Decision Notification’ E_CTR_DEC (IE060) message (having the data element TRANSIT OPERATION-Notification type equal to ‘2-Intention to Control’).
1. The Office of Departure receives a valid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message from the Holder of the Transit Procedure.
1. The MRN is communicated to the Holder of the Transit Procedure with message ‘MRN Allocated’ E_MRN_ALL (IE028).
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.




### Cancellation of the pre-lodged declaration 

**Applicable procedures:** normal and simplified.

<img src="figures/cancel_pre-lodge_dec.svg" alt="Pre-lodgement message flow with cancellation of the pre-lodgement declaration. Flow is described in this section." />

<a href="figures/cancel_pre-lodge_dec.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the Office of Departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The Office of Departure validates this message successfully and sends the ‘Positive Acknowledge’ E_POS_ACK (IE928) message to the Holder of the Transit Procedure to acknowledge receipt of the transit declaration.
1. The Holder of the Transit Procedure decides to cancel the pre-lodged declaration by sending the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message to the Office of Departure.
1. Assuming the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message is valid, the Office of Departure automatically sends a positive decision to cancel the pre-lodged declaration. The ‘Invalidation Decision’ E_INV_DEC (IE009) is sent to the Holder of the Transit Procedure.
1. The transit movement ends.







## Departure message flows

### Standard departure 

**Applicable procedures:** normal and simplified.

<img src="figures/standard_departure.svg" alt="Standard departure message flow. Flow is described in this section." />

<a href="figures/standard_departure.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits a transit declaration to the Office of Departure with the ‘Declaration Data’ E_DEC_DAT (IE015) message.
1. If the transit declaration is valid, the Office of Departure acknowledges the receipt of the transit declaration with the ‘Positive Acknowledge’ E_POS_ACK (IE928) message.
1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.




### Rejection of transit declaration 

**Applicable procedures:** normal and simplified.

<img src="figures/reject_transit_declaration.svg" alt="Rejection of transit declaration. Flow is described in this section." />

<a href="figures/reject_transit_declaration.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits a transit declaration to the Office of Departure with the ‘Declaration Data’ E_DEC_DAT (IE015) message.
2. The Office of Departure validates the declaration data as invalid and thus rejects it by sending a response to the Holder of the Transit Procedure the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message.
3. The transit movement ends.





### Release for transit refused due to guarantee registration failure 

**Applicable procedures:** normal and simplified.

<img src="figures/guarantee_registration_failure.svg" alt="Release for transit refused due to guarantee registration failure. Flow is described in this section." />

<a href="figures/guarantee_registration_failure.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Holder of the Transit Procedure is notified that the declared guarantee is not valid with the ‘Guarantee Not Valid’ E_GUA_INV (IE055) message.
1. The Holder of the Transit Procedure does not send a ‘Declaration Amendment’ E_DEC_AMD (IE013) within the allowed time period. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the Holder of the Transit Procedure.
1. The transit movement ends.






### Release for transit refused for safety and security reasons 


**Applicable procedures:** normal and simplified.

<img src="figures/release_refused_safety_security.svg" alt="Release for transit refused for safety and security reasons. Flow is described in this section." />

<a href="figures/release_refused_safety_security.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. A risk assessment of the transit declaration identifies a high risk with a threat to safety and security. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the Holder of the Transit Procedure.
1. The transit movement ends.




### Declaration amendment accepted/rejected 

**Applicable procedures:** normal and simplified.

<img src="figures/amendment_accepted_rejected.svg" alt="Declaration amendment accepted/rejected. Flow is described in this section." />

<a href="figures/amendment_accepted_rejected.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Holder of the Transit Procedure notifies the Office of Departure of needed changes to the original declaration with a valid ‘Declaration Amendment’ E_DEC_AMD (IE013) before the goods have been released for transit.
1. The Office of Departure performs validation of the IE013 message with one of the following outcomes:
    - The Office of Departure sends the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) to the Holder of the Transit Procedure, who can then send a second ‘Declaration Amendment’ E_DEC_AMD (IE013) message for validation. (Go to step 3.)
    - The Office of Departure successfully validates the IE013 message and sends its acceptance to the Holder of the Transit Procedure with the ‘Amendment Acceptance’ E_AMD_ACC (IE004) message. (Go to step 4.)
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.



### Invalidation request by the holder of the transit procedure before release for transit 

**Applicable procedures:** normal and simplified.

<img src="figures/inval_request_before_release.svg" alt="Invalidation request by the holder of the transit procedure before release for transit. Flow is described in this section." />

<a href="figures/inval_request_before_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Holder of the Transit Procedure is notified with the ‘Guarantee Not Valid’ E_GUA_INV (IE055) message that the declared guarantee is not valid.
1. The Holder of the Transit Procedure decides to invalidate the transit declaration and therefore notifies the Office of Departure with the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message.
1. The Office of Departure examines the request and replies with the positive decision with the ‘Invalidation Decision’ E_INV_DEC (IE009) message (i.e. “Decision” is set to “1=Yes”).
1. The transit movement ends.





### Invalidation request by the holder of the transit procedure after release for transit 

**Applicable procedures:** normal and simplified.

<img src="figures/inval_request_after_release.svg" alt="Invalidation request by the holder of the transit procedure after release for transit. Flow is described in this section." />

<a href="figures/inval_request_after_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The Holder of the Transit Procedure decides to invalidate the transit declaration and therefore notifies the Office of Departure with the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message.
1. The Office of Departure automatically rejects the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) by notifying the Holder of the Transit Procedure with the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message containing the error code ’92-Message out of sequence’.
1. The movement continues to arrivals.




### Invalidation of a transit declaration after release for transit  

**Applicable procedures:** normal and simplified.

<img src="figures/inval_declar_after_release.svg" alt="Invalidation of a transit declaration after release for transit. Flow is described in this section." />

<a href="figures/inval_declar_after_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The ‘Invalidation Decision’ E_INV_DEC (IE009) is sent to the Holder of the Transit Procedure.
1. The transit movement ends.





### Control by Office of Departure with release for transit 

**Applicable procedures:** normal and simplified.

<img src="figures/control_with_release.svg" alt="Control by Office of Departure with release for transit. Flow is described in this section." />

<a href="figures/control_with_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Office of Departure sends the ‘Control Decision Notification’ E_CTR_DEC (IE060) message to the Holder of the Transit Procedure to notify about the upcoming control activities (having the data element TRANSIT OPERATION-Notification type equal to ‘0-Decision to Control (and requested documents if needed)’).
1. The control activity results in one of the following outcomes:
    - Control results are satisfactory. (Go to step 4.) 
    - Control results show minor discrepancies. The Holder of the Transit Procedure communicates a positive release request to the Office of Departure through the ‘Request of Release’ E_REQ_REL (IE054) message. (Go to step 4.)
    - Control results are unsatisfactory and the ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the Holder of the Transit Procedure. The transit movement ends here.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.




### Positive release request with release for transit / negative release request 

**Applicable procedures:** normal and simplified.

<img src="figures/positive_negative_request.svg" alt="Positive release request with release for transit / negative release request. Flow is described in this section." />

<a href="figures/positive_negative_request.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Office of Departure sends the ‘Control Decision Notification’ E_CTR_DEC (IE060) message to the Holder of the Transit Procedure to notify about the upcoming control activities (having the data element TRANSIT OPERATION-Notification type equal to ‘0-Decision to Control (and requested documents if needed)’).
1. The Holder of the Transit Procedure sends the ‘Request of Release’ E_REQ_REL (IE054), containing the flag ‘Release Request’ set to “0-No”, to the Office of Departure.
1. The Office of Departure makes one of the following decisions:
    - The Office of Departure decides to allow the movement to proceed towards release for transit despite the fact that there are minor discrepancies. (Go to step 5.)
    - The Office of Departure decides to refuse release for transit. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the Holder of the Transit Procedure. The transit movement ends here.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.





### Release request rejected  

**Applicable procedures:** normal and simplified.

<img src="figures/release_request_rejected.svg" alt="Release request rejected. Flow is described in this section." />

<a href="figures/release_request_rejected.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Office of Departure sends the ‘Control Decision Notification’ E_CTR_DEC (IE060) message to the Holder of the Transit Procedure to notify about the upcoming control activities (having the data element TRANSIT OPERATION-Notification type equal to ‘0-Decision to Control (and requested documents if needed)’).
1. The Holder of the Transit Procedure sends an invalid ‘Request of Release’ E_REQ_REL (IE054) message.
1. The ‘Request of Release’ E_REQ_REL (IE054) message is rejected with the message ‘Rejection from Office of Departure’ E_DEP_REJ (IE056).
1. The Holder of the Transit Procedure responds in one of the following ways:
    - The Holder of the Transit Procedure does not oppose the minor discrepancies and sends the ‘Request of Release’ E_REQ_REL (IE054) message with the flag ‘Release Request’ set to “1-Yes” to the Office of Departure. (Go to step 7.)
    - The Holder of the Transit Procedure opposes the minor discrepancies and sends the ‘Request of Release’ E_REQ_REL (IE054) message with the flag ‘Release Request’ set to “0-No” to the Office of Departure.
1. The Office of Departure makes one of the following decisions:
    - The Office of Departure decides to allow the movement to proceed towards release for transit despite the fact that there are minor discrepancies. (Go to step 7.)
    - The Office of Departure decides to refuse release for transit. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the Holder of the Transit Procedure. The transit movement ends here.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.




## Arrival message flows

### Standard procedure at destination 

**Applicable procedures:** normal and simplified.

<img src="figures/standard_arrival.svg" alt="Standard arrival message flow. Flow is described in this section." />

<a href="figures/standard_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The goods are released from transit. The Office of Destination sends the ‘Goods Released Notification’ E_GDS_REL (IE025) message to the Trader at Destination.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.




### Simplified procedure at destination 

**Applicable procedures:** simplified.

<img src="figures/simplified_arrival.svg" alt="Simplified arrival message flow. Flow is described in this section." />

<a href="figures/simplified_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message under simplified procedure (simplified procedure flag = ‘Yes’).
1. The Office of Destination notifies the Trader at Destination that the unloading of the goods can be started by means of ‘Unloading Permission’ E_ULD_PER (IE043).
1. After unloading, the Trader at Destination sends the ‘Unloading Remarks’ E_ULD_REM (IE044) to the Office of Destination indicating that the unloading has been completed with no unloading remarks (i.e. the ‘Unloading Remarks’ E_ULD_REM (IE044) message contains the flags Unloading completion = ‘1-Yes’ & Conform = ‘1-Yes’).
1. The goods are released from transit. The Office of Destination sends the ‘Goods Released Notification’ E_GDS_REL (IE025) message to the Trader at Destination.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.



### Rejection of arrival notification 

<img src="figures/reject_arrival.svg" alt="Rejection of arrival notification. Flow is described in this section." />

<a href="figures/reject_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Trader at Destination sends the ‘Arrival Notification’ E_ARR_NOT (IE007) to the Office of Destination and NCTS performs validation of this message. If the ‘Arrival Notification’ E_ARR_NOT (IE007) has been found invalid after validation (i.e. in terms of message structure and R/Cs), NCTS rejects it.
1. The Office of Destination notifies the Trader at Destination by sending the ‘Rejection from Office of Destination’ E_DES_REJ (IE057) message.
1. The Trader at Destination sends another ‘Arrival Notification’ E_ARR_NOT (IE007) to the Office of Destination and NCTS performs validation of this message. This time, the ‘Arrival Notification’ E_ARR_NOT (IE007) has been found valid after validation (i.e. in terms of message structure and R/Cs), NCTS accepts it.



### Unloading Permission Received - Unloading Remarks 

**Applicable procedures:** simplified.

<img src="figures/unload_perm_rec_remarks.svg" alt="Unloading Permission Received - Unloading Remarks. Flow is described in this section." />

<a href="figures/unload_perm_rec_remarks.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The ‘Unloading Permission’ E_ULD_PER (IE043) message is sent to the authorised consignee to allow the unloading at the authorised place.
1. The authorised consignee sends the ‘Unloading Remarks’ E_ULD_REM (IE044) message to the Office of Destination.
1. If no control is decided, or control results are satisfactory, go to step 7.
1. If control is performed at the Office of Destination and major discrepancies are reported into the destination control results: 
    1. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination.
    1. The Office of Departure notifies the Holder of the Transit Procedure that major discrepancies are reported in the destination control results with the ‘Discrepancies’ E_DIS_SND (IE019) message. Go to step 7.
1. If unloading is not completed and the Office of Destination decides to allow unloading to continue:
    1. The Office of Destination sends a new ‘Unloading Permission’ E_ULD_PER (IE043) message.
    1. The authorized consignee sends the ‘Unloading Remarks’ E_ULD_REM (IE044) message to the Office of Destination.
1. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination in order to notify them that the transit procedure has ended successfully.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.

### Unloading remarks rejected 

**Applicable procedures:** simplified.

<img src="figures/unload_remarks_reject.svg" alt="Unloading remarks rejected. Flow is described in this section." />

<a href="figures/unload_remarks_reject.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message under simplified procedure (simplified procedure flag = ‘Yes’).
1. The Office of Destination notifies the Trader at Destination that the unloading of the goods can be started by means of ‘Unloading Permission’ E_ULD_PER (IE043).
1. The Trader at Destination sends an invalid ‘Unloading Remarks’ E_ULD_REM (IE044) message to the Office of Destination.
1. The Office of Destination rejects these remarks by sending back a ‘Rejection from Office of Destination’ E_DES_REJ (IE057) message.
1. The Trader at Destination re-sends the ‘Unloading Remarks’ E_ULD_REM (IE044) message until it is acceptable to the Office of Destination.
1. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination in order to notify them that the transit procedure has ended successfully.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.

### Major Discrepancies found during control at the Office of Destination - Resolved before the expiration of resolution timer 

**Applicable procedures:** normal and simplified.

<img src="figures/discrep_res_before_timer_expire.svg" alt="Major Discrepancies found during control at the Office of Destination - Resolved before the expiration of resolution timer. Flow is described in this section." />

<a href="figures/discrep_res_before_timer_expire.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The Office of Destination performs control and major discrepancies are reported.
1. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination.
1. The Office of Departure notifies the Holder of the Transit Procedure that major discrepancies are reported in the destination control results with the ‘Discrepancies’ E_DIS_SND (IE019) message.
1. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination in order to notify them that the transit procedure has ended successfully.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.

### Major Discrepancies found during control at the Office of Destination - Major Discrepancies are confirmed - Recovery to be started 

**Applicable procedures:** normal and simplified.

<img src="figures/discrep_confirm_recovery.svg" alt="Major Discrepancies found during control at the Office of Destination - Major Discrepancies are confirmed - Recovery to be started. Flow is described in this section." />

<a href="figures/discrep_confirm_recovery.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The Office of Destination performs control and major discrepancies are reported that justify recovery.
1. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination in order to notify them that the transit procedure has ended successfully.
1. The Office of Departure notifies the Holder of the Transit Procedure that major discrepancies are reported in the destination control results with the ‘Discrepancies’ E_DIS_SND (IE019) message.
1. The movement continues with recovery.




### Major Discrepancies found during control at the Office of Destination - Resolved after the expiration of resolution timer 

**Applicable procedures:** normal and simplified.

<img src="figures/discrep_res_after_expire.svg" alt="Major Discrepancies found during control at the Office of Destination - Resolved after the expiration of resolution timer. Flow is described in this section." />

<a href="figures/discrep_res_after_expire.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The Office of Destination performs control and major discrepancies are reported.
1. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination.
1. The Office of Departure notifies the Holder of the Transit Procedure that major discrepancies are reported in the destination control results with the ‘Discrepancies’ E_DIS_SND (IE019) message.
1. After expiration of the resolution timer, the discrepancies are resolved. The Office of Destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the Trader at Destination in order to notify them that the transit procedure has ended successfully.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.




## Other message flows
