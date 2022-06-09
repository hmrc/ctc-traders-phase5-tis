---
title: NCTS Phase 5 Technical Interface Specification
weight: 1
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---

# NCTS Phase 5 Technical Interface Specification

Version 0.0.1a issued June 2022

***

DOCUMENT SUMMARY
This document is the first part of the Technical Interface Specification (TIS) for Direct Trader Input (DTI) to NCTS. 
 
It shows the processes involved in the exchange of messages between traders and the NCTS system at departure and arrival of transit movements, and provides definitions, formats and validations of those messages.  

***

## Introduction
 
The New Computerised Transit System (NCTS) is a European wide system, based upon electronic declaration and processing, designed to provide better management and control of Union and Common Transit. It involves all countries comprising the EU Member States and all Common Transit Convention contracting countries.

The NCTS systems of all National Administrations are connected to each other via a central domain in Brussels. This allows the details and progress of a transit movement to be monitored by all actors concerned at every stage.

The main objectives of the NCTS are:

- to increase the efficiency and effectiveness of transit procedures
- to improve both the prevention and detection of fraud
- to accelerate transactions carried out under a transit procedure and to offer security for them

In order to use the NCTS, traders need the facility to send and receive electronic messages to and from the UK - NCTS. Connected traders receive electronic responses advising of key decisions during both departure and destination, such as:

- acceptance of declaration
- release of goods
- notification of discharge of liability, that is the release of the guarantee which is in place thoughout the lifespan of the movement in order to cover the duties at risk during the movement of goods

Traders cannot interface directly with the NCTS to input or amend data or to access records and reference data, but simply exchange defined structured messages with the system. 

In certain circumstances, where Simplified NCTS Procedures are used by Authorised Consignors/Consignees, processing and release will be automatic and allow, depending upon the conditions of authorisation, for 'out of hours' clearance. This will allow for selective, risk-based controls, and for the processing of declarations and the release of goods to become largely automatic.

### Scope

This document gives an overview of the processes involved in the exchange of NCTS messages with traders and defines the messages associated with NCTS, in particular:

- the trader’s declaration for Transit and associated Customs response
- control and release of the movement at departure 
- the trader’s notification of arrival and associated Customs response
- control and release of the goods at destination
- registration of any incidents that may occur en route
 
These messages are developed following the Functional Transit System Specification (FTSS) and Design Documentation for National Transit Application (DDNTA) documents distributed by the EU Commission to National Administrations.

### NCTS Reference Data

NCTS holds two types of reference data:

- common reference data which is held on a central system known as Common Services Reference Data (CS/RD2) which is applicable to all contracting parties’ NCTS systems. It is used to validate specific fields within trader messages and ensure that they contain acceptable data.
- national reference data which applies locally to the systems of individual countries. This is used to validate traders’ details, guarantee information and any authorisations they may hold when submitted in traders messages.

#### CS/RD2

Reference data within CS/RD2 is made of code lists. Each code list provides data which is used for validation against specific fields within declarations submitted by users, and also within intra NCTS system message exchange. The latest CS/RD2 data is released overnight on a daily basis. The most volatile code list contained within CS/RD2 is CL 141 Customs Offices, which holds details of all valid Customs Offices for all Common Transit Convention countries and all the transit functions available per office, such as Office of Departure (DEP), Office of Destination (DES) and Office of Transit (TRA).

It is essential that any software solution developed for traders retrieves these updates on a daily basis to ensure any validation coded in to the software is synchronised with UK NCTS to prevent unnecessary rejections.

#### National Reference Data

This is administered by each National Administration on its own behalf. When a trader applies to use the transit procedure, specific data is captured into NCTS which includes the trader’s name and address, their EORI number, details about guarantees for transit usage that they hold and in the case of Authorised Consignors/Consignees details of their authorised locations and their allocated code numbers. Where these details are used by the trader within their declaration they will be validated against the national reference data held by NCTS.  

### UK NCTS

The UK NCTS system is made up of two separate NCTS cores, one processes Great Britain mainland transit movements whilst the other processes transit movements within Northern Ireland.

The two cores have different modes of operation. The Great Britain mainland NCTS core operates in Common Transit mode. This means that where a rule or condition has different applicability dependent on whether the country of departure/destination/transit is a within the territory of the European Union or a separate Common Transit country, then that rule or condition will be applied to Great Britain mainland as being a common transit country. Conversely, the Northern Ireland NCTS core operates in Union Transit mode meaning that a territory dependent rule or condition will be applied to Northern Ireland as if it were part of EU territory.

This is an important consideration if you intend to implement any rules or conditions to validate declarations for you or your customers.

Both cores have entirely separate common and national reference data. As a result of this, the Great Britain mainland and Northern Ireland NCTS services operate with separate country codes:

- Great Britain mainland NCTS uses **GB** as its country prefix
- Northern Ireland NCTS uses **XI** as its country prefix

NCTS needs region specific reference data, such as Customs Office codes, guarantee reference numbers and Economic Operator Registration and Identification (EORI) (also known as the Trader Identification Number) to include the applicable country code.

Where located in Great Britain mainland, Customs Offices, traders’ EORIs and related guarantees have the GB prefix. For example, Dover port has the office code GB000060.

Where located in Northern Ireland, Customs Offices, traders EORIs and related guarantees have the XI prefix. For example, the Belfast Entry Process Unit has the office code XI000142.

Additionally, authorised locations used by Authorised Consignors and Consignees exist only in the NCTS appropriate to their physical location.

Because authorised location codes are linked to the Authorised Consignor/nees’ EORI, and because EORIs are linked to the procedure holder’s guarantee, the software you develop should allow both the use of GB EORIs and their associated GB guarantee as well as XI EORIS and their associated XI guarantee.

Despite there being two separate cores in operation, there is only one submission channel used to access UK NCTS. You can submit Great Britain mainland or Northen Ireland messages without the need to add any routing information whatsoever. Your messages will automatically be routed to the correct core by a logic layer embedded in the API. 

### Access to UK NCTS

Traders may exchange XML messages with both NCTS systems via the CTC trader API channel. This allows 3rd party developer software to send and receive arrival and departure notifications using XML language for the message payload. The CTC trader API provides full Great Britain mainland and Northern Ireland integration and a single endpoint for both Great Britain mainland and Northern Ireland declarations. 

Full details regarding connection to the existing submission channel and technical message formatting information are contained in the Technical Interface Specifications (TIS) Appendices.

### Liability Amount for Guarantees

Guarantee usage monitoring in NCTS requires that a liability reference amount is recorded against each guarantee in a declaration.

Departure declarations submitted by users (IE015 message) can only contain guarantee reference amounts in respect of guarantee types 0,1,2,4 and 9. For all other guarantee types Border Force will enter the reference amount into NCTS manually prior to releasing the movement.

In exceptional circumstances, where a declarant is unable to determine the guarantee reference amount, the Common Transit Convention allows the amount to be fixed at 10,000 euros for each transit operation.

If the departure declaration does not contain a guarantee reference amount and guarantee being used is either type 0, 1, 2, 4 or 9, then the system automatically inserts 10,000 euros as the guarantee liability amount.

This applies in all circumstances except for national transit movements, for example, Great Britain to Great Britain. National transit is not supported by the Common Transit Convention however, UK national legislation allows its usage as a trade facilitation.

### TAD (Transit Accompanying Document) / TSAD (Transit Security Accompanying Document)

A TSAD is needed for declarations containing safety and security data. A TAD is required for all other declarations. **TADs/TSADs must only be created using information from the IE029 message.**

TADs/TSADs are electronically authenticated by NCTS. This means that the TAD/TSAD does not need to be authenticated by the Office of Departure by stamp. The CT movement is not **legally** released from transit until the IE029 has been generated by Customs and a valid TAD/TSAD subsequently created. 

**The TAD/TSAD should only be created using data that has been validated or provided by the NCTS system. This can be achieved by generating the TAD/TSAD direct from the IE029 message either electronically or through printing it manually, or by using data from the IE029 to update a previously created and validated transit record, and then creating the TAD/TSAD from that.**

Traders using the Normal procedure will have the option either to collect the TAD/TSAD from the Office of Departure or to generate the TAD/TSAD at their own premises. Approval to create the TAD/TSAD is granted by the CCTO, to whom the trader’s application must be submitted for consideration. The trader must provide evidence of their ability to create the TAD/TSAD in the required format.
Traders authorised to use Simplified NCTS Procedures as Authorised Consignors can generate their own TAD/TSAD as part of their authorisation permission. 

####Fallback procedure  

Authorised Consignors are obliged to hold special stamps to authenticate documents in case of system failure so they can authorise their own fallback documents. Authorised Consignors additionally require a Commission approved stamp that informs the Office of Destination that fallback has been used.

####Manually printing TADs/TSADs

For the specifications on the printing of a paper TAD, see **Guidelines for printing a TAD** – these are contained in **Part IV, Chapter 2, Annexes 8.1 and 8.2 of the European Commission’s Transit Manual** in the following hyperlink:

https://ec.europa.eu/taxation_customs/system/files/2021-06/transit_manual_june_2020_en.pdf

For the specifications on the printing of the paper TSAD, see **Guidelines For Print Out of TSAD, Printing Guidelines for TSAD and TSAD and LoI**.

The IE029 will specify the number of copies required in the case of a printed TAD/TSAD. If a return copy is required, i.e. in the case HEADER.NCTS return copy is set, then two copies of the TAD/TSAD will be required; if not, only one needs to be printed. The return copy is required when the Office of Destination (OoDest) is not using the NCTS yet.

The ‘liability amount’ information in the guarantee data group is not printed on the TAD/TSAD.

If a declaration contains only one goods item, all the information for the movement is included in the TAD. If the declaration contains more than one goods item, all the goods items are included on the LoI (List of Items). However, if the declaration contains safety and security data, the goods item information (even if there is only one goods item) is always included on the TSAD LoI.  

The printer and print driver, used for printing the TAD/TSAD, must be capable of printing a bar code of standard ISO code 128 set B (but not EAN128). 
The font type is BC C128 Narrow (True Type) version 2.0.

### Important phase 5 terms

The following terms are important to understand in phase 5:

- **Consignment:** The header information is provided and applies to the whole transit declaration (up to 1 Consignment level per declaration).

- **House Consignment:** The lowest transport information is provided, and this applies to all its Consignment Items (each Consignment can contain up to 99 House Consignments).

    The House Consignment level covers information relating to all goods that are subject to the same house transport contract. A house transport contract is a transport contract with a freight forwarder, non-vessel or aircraft operating common carrier or his agent or a postal operator. Where several house transport contracts exist, the information provided in customs declarations, notifications and proof of the customs status as Union Goods should relate to the lowest level of contracts. This is usually the contract concluded by a freight forwarder and the shipper.

    The new House Consignment level is introduced to give more flexibility to the Economic Operators, allowing them to lodge one declaration with several Consignors/Consignees.

- **Consignment Item:** The items information is provided (each House Consignment can contain up to 999 Consignment Items).

## Process flows

### Functional errors

It should be noted that the following messages are used to report functional errors:

- Rejection from Office of Departure (IE056: E_DEP_REJ);
- Rejection from Office of Destination (IE057: E_DES_REJ).

A functional error occurs in the following circumstances:

- missing required data from an IE message
- IE message completed incorrectly
- missing data group(s)
- data item(s) violates a code list
- out of sequence message(s).

### Pre-lodgement message flows

#### Transit presentation notification valid 

**Applicable procedures:** normal and simplified.

This scenario involves the submission of a valid transit declaration for goods that have not yet been presented to the office of departure.

<img src="figures/trans_pres_notif_valid.svg" alt="Pre-lodgement message flow with presentation of a valid notification. Flow is described in this section." />

<a href="figures/trans_pres_notif_valid.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the holder of the transit procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the office of departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The office of departure validates this message successfully and sends the ‘Positive Acknowledgement’ E_POS_ACK (IE928) message to the holder of the transit procedure to acknowledge receipt of the transit declaration.
1. Following the result of the risk analysis engine, the office of departure may select the pre-lodged declaration for potential control of the goods prior to their presentation. The following control decisions are possible: 
    - **Yes** (apply control): the office of departure notifies the holder of the transit procedure (provided that they are an AEO) about the intention to potentially control the goods, via the ‘Control Decision Notification’ E_CTR_DEC (IE060) message (having the data element TRANSIT OPERATION-Notification type equal to ‘2-Intention to Control’). Go to step 4.
    - **No** (no control): Go to step 4.
1. The office of departure receives a valid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message from the holder of the transit procedure.
1. The MRN is communicated to the holder of the transit procedure with message ‘MRN Allocated’ E_MRN_ALL (IE028).
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The departure process ends.



#### Transit presentation not valid 

**Applicable procedures:** normal and simplified.

This scenario involves the submission of an invalid transit declaration for goods that have not yet been presented to the office of departure.

<img src="figures/trans_pres_notif_not_valid.svg" alt="Pre-lodgement message flow with presentation of a non-valid notification. Flow is described in this section." />

<a href="figures/trans_pres_notif_not_valid.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the holder of the transit procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the office of departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The office of departure validates this message successfully and sends the ‘Positive Acknowledgement’ E_POS_ACK (IE928) message to the holder of the transit procedure to acknowledge receipt of the transit declaration.
1. The office of departure receives an invalid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message from the holder of the transit procedure.
1. The office of departure decides to reject the E_PRE_NOT (IE170) message. 
1. The office of departure notifies the holder of the transit procedure with the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message.
1. If the time limit expires without the holder of the transit procedure resending a valid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message, the holder of the transit procedure is notified with the message ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) by the office of departure.
1. The transit movement ends.



#### Corrections of the pre-lodgement declaration prior to presentation of the goods 

**Applicable procedures:** normal and simplified.

This scenario involves the holder of the transit procedure making corrections to the transit declaration prior to presentation of the goods.

<img src="figures/correct_pre-lodge_dec_prior_pres_goods.svg" alt="Pre-lodgement message flow with corrections of the pre-lodgement declaration prior to presentation of the goods. Flow is described in this section." />

<a href="figures/correct_pre-lodge_dec_prior_pres_goods.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the holder of the transit procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the office of departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The office of departure validates this message successfully and sends the ‘Positive Acknowledgement’ E_POS_ACK (IE928) message to the holder of the transit procedure to acknowledge receipt of the transit declaration.
1. The holder of the transit procedure decides to correct the transit declaration and submits the ‘Declaration Amendment’ E_DEC_AMD (IE013) message.
1. The office of departure performs validation of the IE013 message with one of the following outcomes:
    - **No** (IE013 not valid): The office of departure sends the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) to the holder of the transit procedure. Go to step 3.
    - **Yes** (IE013 is valid): The office of departure sends its acceptance to the holder of the transit procedure with the ‘Amendment Acceptance’ E_AMD_ACC (IE004) message. Go to step 5.
1. Following the result of the Risk Analysis engine, the office of departure may select the pre-lodged declaration for potential control of the goods prior to their presentation. The following outcomes are possible: 
    - **Yes** (apply control): The office of departure notifies the holder of the transit procedure (provided that they are an AEO) about the intention to potentially control the goods, via the ‘Control Decision Notification’ E_CTR_DEC (IE060) message (having the data element TRANSIT OPERATION-Notification type equal to ‘2-Intention to Control’).
    - **No** (no control): Go to step 6.
1. The office of departure receives a valid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message from the holder of the transit procedure.
1. The MRN is communicated to the holder of the transit procedure with message ‘MRN Allocated’ E_MRN_ALL (IE028).
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The departure process ends.




#### Cancellation of the pre-lodged declaration 

**Applicable procedures:** normal and simplified.

This scenario involves the holder of the transit procedure cancelling the pre-lodged transit declaration.

<img src="figures/cancel_pre-lodge_dec.svg" alt="Pre-lodgement message flow with cancellation of the pre-lodgement declaration. Flow is described in this section." />

<a href="figures/cancel_pre-lodge_dec.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the holder of the transit procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the office of departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The office of departure validates this message successfully and sends the ‘Positive Acknowledgement’ E_POS_ACK (IE928) message to the holder of the transit procedure to acknowledge receipt of the transit declaration.
1. The holder of the transit procedure decides to cancel the pre-lodged declaration. 
1. The holder of the transit procedure sends the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message to the office of departure.
1. Assuming the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message is valid, the office of departure automatically sends a positive decision to cancel the pre-lodged declaration. The ‘Invalidation Decision’ E_INV_DEC (IE009) is sent to the holder of the transit procedure.
1. The transit movement ends.







### Departure message flows

#### Standard departure 

**Applicable procedures:** normal and simplified.

This scenario outlines the basic standard transit procedure at departure when the goods are presented without delay by the holder of the transit procedure.

<img src="figures/standard_departure.svg" alt="Standard departure message flow. Flow is described in this section." />

<a href="figures/standard_departure.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the holder of the transit procedure submits a transit declaration to the office of departure with the ‘Declaration Data’ E_DEC_DAT (IE015) message.
1. If the transit declaration is valid, the office of departure acknowledges the receipt of the transit declaration with the ‘Positive Acknowledgement’ E_POS_ACK (IE928) message.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The departure process ends.




#### Rejection of transit declaration 

**Applicable procedures:** normal and simplified.

This scenario shows the case when the transit declaration is rejected. Before submission of the transit declaration, the state of the movement at the office of departure is “None”.

<img src="figures/reject_transit_declaration.svg" alt="Rejection of transit declaration. Flow is described in this section." />

<a href="figures/reject_transit_declaration.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the holder of the transit procedure submits a transit declaration to the office of departure with the ‘Declaration Data’ E_DEC_DAT (IE015) message.
2. The office of departure validates the declaration data as invalid and thus rejects it by sending a response to the holder of the transit procedure the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message.
3. The transit movement ends.





#### Release for transit refused due to guarantee check failure 

**Applicable procedures:** normal and simplified.

This scenario involves the case when the release for transit is refused because the result of the guarantee check is not successful.

<img src="figures/guarantee_registration_failure.svg" alt="Release for transit refused due to guarantee registration failure. Flow is described in this section." />

<a href="figures/guarantee_registration_failure.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when an IE015 message is sent and an IE928 message is sent back.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The holder of the transit procedure is notified that the declared guarantee is not valid with the ‘Guarantee Not Valid’ E_GUA_INV (IE055) message.
1. The holder of the transit procedure does not send a ‘Declaration Amendment’ E_DEC_AMD (IE013) within the allowed time period. 
1. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the holder of the transit procedure.
1. The transit movement ends.






#### Release for transit refused for safety and security reasons 


**Applicable procedures:** normal and simplified.

This scenario involves the case when the release for transit is refused because of safety and security concerns.

<img src="figures/release_refused_safety_security.svg" alt="Release for transit refused for safety and security reasons. Flow is described in this section." />

<a href="figures/release_refused_safety_security.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when an IE015 message is sent and an IE928 message is sent back.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. A risk assessment of the transit declaration identifies a high risk with a threat to safety and security. 
1. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the holder of the transit procedure.
1. The transit movement ends.




#### Declaration amendment accepted/rejected 

**Applicable procedures:** normal and simplified.

This scenario involves the cases when valid and invalid declaration amendments are made.

<img src="figures/amendment_accepted_rejected.svg" alt="Declaration amendment accepted/rejected. Flow is described in this section." />

<a href="figures/amendment_accepted_rejected.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when an IE015 message is sent and an IE928 message is sent back.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The holder of the transit procedure notifies the office of departure of needed changes to the original declaration with a valid ‘Declaration Amendment’ E_DEC_AMD (IE013) before the goods have been released for transit.
1. The office of departure performs validation of the IE013 message with one of the following outcomes:
    - **No** (IE013 not valid): The office of departure sends the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) to the holder of the transit procedure. Go to step 3.
    - **Yes** (IE013 is valid): The office of departure sends its acceptance to the holder of the transit procedure with the ‘Amendment Acceptance’ E_AMD_ACC (IE004) message. Go to step 5.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The departure process ends.



#### Cancellation request by the holder of the transit procedure before release for transit 

**Applicable procedures:** normal and simplified.

This scenario involves the case when the holder of the transit procedure makes a cancellation request before release for transit.

<img src="figures/inval_request_before_release.svg" alt="Cancellation request by the holder of the transit procedure before release for transit. Flow is described in this section." />

<a href="figures/inval_request_before_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when an IE015 message is sent and an IE928 message is sent back.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The holder of the transit procedure decides to cancel the transit declaration and therefore notifies the office of departure with the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message.
1. The office of departure examines the request and replies with the positive decision with the ‘Invalidation Decision’ E_INV_DEC (IE009) message (i.e. “Decision” is set to “1=Yes”).
1. The transit movement ends.





#### Cancellation request by the holder of the transit procedure after release for transit 

**Applicable procedures:** normal and simplified.

This scenario involves the case when the holder of the transit procedure makes a cancellation request after release for transit.

<img src="figures/inval_request_after_release.svg" alt="Cancellation request by the holder of the transit procedure after release for transit. Flow is described in this section." />

<a href="figures/inval_request_after_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when an IE015 message is sent and an IE928 message is sent back.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The holder of the transit procedure decides to cancel the transit declaration and therefore notifies the office of departure with the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message.
1. The office of departure automatically rejects the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) by notifying the holder of the transit procedure with the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message containing the error code ’92-Message out of sequence’.
1. The movement continues to arrivals.




#### Cancellation of a transit declaration after release for transit  

**Applicable procedures:** normal and simplified.

This scenario involves the case when a transit declaration is cancelled by Border Force at the office of departure after the goods are released for transit.

<img src="figures/inval_declar_after_release.svg" alt="Cancellation of a transit declaration after release for transit. Flow is described in this section." />

<a href="figures/inval_declar_after_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when an IE015 message is sent and an IE928 message is sent back.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The office of departure decides to cancel the declaration.
1. The ‘Invalidation Decision’ E_INV_DEC (IE009) is sent to the holder of the transit procedure.
1. The transit movement ends.





#### Control by office of departure 

**Applicable procedures:** normal and simplified.

This scenario outlines what happens when the office of departure decides to initiate control on a transit movement.

<img src="figures/control_with_release.svg" alt="Control by office of departure with release for transit. Flow is described in this section." />

<a href="figures/control_with_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when an IE015 message is sent and an IE928 message is sent back.
1. The office of departure communicates the MRN to the holder of the transit procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The office of departure sends the ‘Control Decision Notification’ E_CTR_DEC (IE060) message to the holder of the transit procedure to notify about the upcoming control activities (having the data element TRANSIT OPERATION-Notification type equal to ‘0-Decision to Control (and requested documents if needed)’).
1. The control activity results in one of the following outcomes:
    - Control results are satisfactory. Go to step 5. 
    - Control results are unsatisfactory and the ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the holder of the transit procedure. The transit movement ends here.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The departure process ends.


### Arrival message flows

#### Normal procedure at destination 

**Applicable procedures:** normal.

This scenario outlines the basic standard transit procedure at arrival.

<img src="figures/standard_arrival.svg" alt="Standard arrival message flow. Flow is described in this section." />

<a href="figures/standard_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the office of destination, the trader at destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The goods are released from transit. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination.
1. The office of departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the holder of the transit procedure at departure.
1. The arrivals process ends.



#### Simplified procedure at destination 

**Applicable procedures:** simplified.

This scenario outlines the scenario when the trader at destination sends an arrival notification E_ARR_NOT (IE007) message under simplified procedure.

<img src="figures/simplified_arrival.svg" alt="Simplified arrival message flow. Flow is described in this section." />

<a href="figures/simplified_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the office of destination, the trader at destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message under simplified procedure (simplified procedure flag = ‘Yes’).
1. The office of destination notifies the trader at destination that the unloading of the goods can be started by means of ‘Unloading Permission’ E_ULD_PER (IE043).
1. After unloading, the trader at destination sends the ‘Unloading Remarks’ E_ULD_REM (IE044) to the office of destination indicating that the unloading has been completed with no unloading remarks (i.e. the ‘Unloading Remarks’ E_ULD_REM (IE044) message contains the flags Unloading completion = ‘1-Yes’ & Conform = ‘1-Yes’).
1. The goods are released from transit. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination.
1. The office of departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the holder of the transit procedure at departure.
1. The arrivals process ends.



#### Rejection of arrival notification 

This scenario outlines what happens when the arrival notification is not valid.

<img src="figures/reject_arrival.svg" alt="Rejection of arrival notification. Flow is described in this section." />

<a href="figures/reject_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. The trader at destination sends the ‘Arrival Notification’ E_ARR_NOT (IE007) to the office of destination. 
1. NCTS performs validation of this message. The following outcomes are possible:
    - **Yes** (the message is valid). Go to step 5.
    - **No** (the message is not valid). Go to step 3.
1. If the ‘Arrival Notification’ E_ARR_NOT (IE007) has been found to be invalid (that is, in terms of message structure and R/Cs), NCTS rejects it.
1. The office of destination notifies the trader at destination by sending the ‘Rejection from Office of Destination’ E_DES_REJ (IE057) message. Go to step 1.
1. If the ‘Arrival Notification’ E_ARR_NOT (IE007) has been found to be valid (i.e. in terms of message structure and R/Cs), NCTS accepts it.
1. The ‘Unloading Permission’ E_ULD_PER (IE043) message is sent to the authorised consignee to allow the unloading at the authorised place.
1. The authorised consignee sends the ‘Unloading Remarks’ E_ULD_REM (IE044) message to the office of destination.
1. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination in order to notify them that the transit procedure has ended successfully.
1. The office of departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the holder of the transit procedure.
1. The arrivals process ends.



#### Unloading Permission Received - Unloading Remarks 

**Applicable procedures:** simplified.

This scenario outlines what happens when the authorized consignee sends the
unloading remarks E_ULD_REM (IE044) message.

<img src="figures/unload_perm_rec_remarks.svg" alt="Unloading Permission Received - Unloading Remarks. Flow is described in this section." />

<a href="figures/unload_perm_rec_remarks.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the office of destination, the trader at destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The ‘Unloading Permission’ E_ULD_PER (IE043) message is sent to the authorised consignee to allow the unloading at the authorised place.
1. The authorised consignee sends the ‘Unloading Remarks’ E_ULD_REM (IE044) message to the office of destination.
1. If no control is decided, or control results are satisfactory, go to step 7.
1. If control is performed at the office of destination and major discrepancies are reported into the destination control results: 
    1. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination.
    1. The office of departure notifies the holder of the transit procedure at departure that major discrepancies are reported in the destination control results with the ‘Discrepancies’ E_DIS_SND (IE019) message. Go to step 7.
1. If unloading is not completed and the office of destination decides to allow unloading to continue:
    1. The office of destination sends a new ‘Unloading Permission’ E_ULD_PER (IE043) message.
    1. The authorized consignee sends the ‘Unloading Remarks’ E_ULD_REM (IE044) message to the office of destination.
1. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination in order to notify them that the transit procedure has ended successfully.
1. The office of departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the holder of the transit procedure.
1. The arrivals process ends.

#### Unloading remarks rejected 

**Applicable procedures:** simplified.

This scenario outlines what happens when the office of destination rejects an invalid unloading remarks message.

<img src="figures/unload_remarks_reject.svg" alt="Unloading remarks rejected. Flow is described in this section." />

<a href="figures/unload_remarks_reject.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the office of destination, the trader at destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message under simplified procedure (simplified procedure flag = ‘Yes’).
1. The office of destination notifies the trader at destination that the unloading of the goods can be started by means of ‘Unloading Permission’ E_ULD_PER (IE043).
1. The trader at destination sends an ‘Unloading Remarks’ E_ULD_REM (IE044) message to the office of destination.
1. The office of destination checks the validity of the message. The following outcomes are possible:
    - **No** (message not valid): The office of destination rejects these remarks by sending back a ‘Rejection from Office of Destination’ E_DES_REJ (IE057) message. Go to step 3.
    - **Yes** (message is valid): Go to step 5. 
1. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination in order to notify them that the transit procedure has ended successfully.
1. The office of departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the holder of the transit procedure.
1. The arrivals process ends.

#### Major discrepancies found during control at the office of destination

**Applicable procedures:** normal.

This scenario outlines how major discrepancies found during control at the office of destination are either resolved before expiration of the resolution timer or result in recovery.

<img src="figures/discrep_res_before_timer_expire.svg" alt="Major Discrepancies found during control at the office of destination - Resolved before the expiration of resolution timer. Flow is described in this section." />

<a href="figures/discrep_res_before_timer_expire.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the office of destination, the trader at destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The office of destination performs control and major discrepancies are reported.
1. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination.
1. The office of departure notifies the holder of the transit procedure at departure that major discrepancies are reported in the destination control results with the ‘Discrepancies’ E_DIS_SND (IE019) message.
1. The following outcomes are possible:
    - The major discrepancies are not resolved. Go to step 6.
    - The major discrepancies are resolved. Go to step 7.
1. The competent authority of recovery at departure notifies the holder of the transit procedure with the ‘Recovery Notification’ E_REC_NOT (IE035) message.
1. The office of destination sends the ‘Goods Release Notification’ E_GDS_REL (IE025) message to the trader at destination in order to notify them that the transit procedure has ended successfully.
1. The office of departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the holder of the transit procedure.
1. The arrivals process ends.

### Recovery message flows

#### Recovery process

This scenario shows the recovery process for non-arrival of goods.

<img src="figures/recovery_process.svg" alt="Recovery initiation on incident occurrence message flow. Flow is described in this section." />

<a href="figures/recovery_process.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the holder of the transit procedure.
1. The competent authority of recovery at departure notifies the holder of the transit procedure with the ‘Recovery Notification’ E_REC_NOT (IE035) message.
1. The ‘Write-off Notification’ E_WRT_NOT (IE045) message is sent to the holder of the transit procedure.
1. The transit movement ends.

#### Recovery initiation on incident occurrence

This scenario shows what happens when the competent authority of recovery at departure
decides to start recovery due to the occurrence of incidents during the journey of the transit
movement.

<img src="figures/recovery_incident.svg" alt="Recovery initiation on incident occurrence message flow. Flow is described in this section." />

<a href="figures/recovery_incident.svg" target="_blank">Open the diagram in a new tab.</a>

1. The process starts when the office of departure forwards the incident information to the holder of the transit procedure through the ‘Forwarded Incident Notification To ED’ E_INC_NOT (IE182) message.
1. The officer decides to update the system to recommend recovery due to suspicion of fraud or any other irregularity.
1. The competent authority of recovery at departure notifies the holder of the transit procedure with the ‘Recovery Notification’ E_REC_NOT (IE035) message.
1. The ‘Write-off Notification’ E_WRT_NOT (IE045) message is sent to the holder of the transit procedure.
1. The transit movement ends.

### Guarantee message flows

#### Guarantee query check

This scenario shows how at any point in time, the holder of the transit procedure or the guarantor can make guarantee queries to the Guarantee Management System to check the details of their
own guarantees even though no MRN may have been allocated to the transit movement yet.

<img src="figures/guarantee_check.svg" alt="Guarantee query check message flow. Flow is described in this section." />

<a href="figures/guarantee_check.svg" target="_blank">Open the diagram in a new tab.</a>

1. The holder of the transit procedure sends a JSON guarantee balance request. 
1. The JSON guarantee balance request is converted internally to an appropriate ‘Query on Guarantees’ E_GUA_QUE (IE034) message, which is sent to the Guarantee Management System. 
1. The Guarantee Management System replies back internally with the ‘Response Query on Guarantees’ E_GUA_RSP (IE037) message.
1. The ‘Response Query on Guarantees’ E_GUA_RSP (IE037) message is converted internally to a JSON guarantee balance response, which is sent to the holder of the transit procedure.


