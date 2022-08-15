---
title: NCTS Phase 5 Technical Interface Specification
weight: 1
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---

# NCTS Phase 5 Technical Interface Specification

Version 0.3 issued August 2022
***


## Document summary

This document is the first part of the Technical Interface Specification (TIS) for Direct Trader Input (DTI) to NCTS. 
 
It shows the processes involved in the exchange of messages between traders and the NCTS system at departure and arrival of transit movements, and provides definitions, formats and validations of those messages.  


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

Because authorised location codes are linked to the Authorised Consignor/nees’ EORI, and because EORIs are linked to the procedure holder’s guarantee, the software you develop should allow both the use of GB EORIs and their associated GB guarantee as well as XI EORIs and their associated XI guarantee.

Despite there being two separate cores in operation, there is only one submission channel used to access UK NCTS. You can submit Great Britain mainland or Northen Ireland messages without the need to add any routing information whatsoever. Your messages will automatically be routed to the correct core by a logic layer embedded in the API. 

### Access to UK NCTS

Traders may exchange XML messages with both NCTS systems via the CTC trader API channel. This allows 3rd party developer software to send and receive arrival and departure notifications using XML language for the message payload. The CTC trader API provides full Great Britain mainland and Northern Ireland integration and a single endpoint for both Great Britain mainland and Northern Ireland declarations. 

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

#### Fallback procedure  

Authorised Consignors are obliged to hold special stamps to authenticate documents in case of system failure so they can authorise their own fallback documents. Authorised Consignors additionally require a Commission approved stamp that informs the Office of Destination that fallback has been used.

#### Manually printing TADs/TSADs

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

