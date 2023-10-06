---
title: NCTS Phase 5 Technical Interface Specification
weight: 1
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---

# NCTS Phase 5 Technical Interface Specification

Version 15.0 issued 11 October 2023

Based on NCTS5 document version 5.15.1-v1.00 and issue date 7 March 2023

------

## NCTS5 key dates

The following dates are subject to change. You should monitor this section regularly.

| Event                            | Date(s)                     |
| -------------------------------- | --------------------------- |
| UK NCTS5 service go-live         | 1 July 2024                 |
| UK cutover from NCTS4 to NCTS5   | 1 July 2024 to 15 July 2024 |
| NCTS5 transition period end date | 21 January 2025             |

## Document summary

This document is the first part of the Technical Interface Specification (TIS) for Direct Trader Input (DTI) to the New Computerised Transit System (NCTS). 

It shows the processes involved in the exchange of messages between traders and the NCTS at departure and arrival of transit movements, and provides definitions, formats and validations of those messages.

## Introduction

The NCTS is a Europe-wide system that is based on electronic declaration and processing and is designed to provide better management and control of Union and Common Transit. It involves all European Union (EU) member states and all Common Transit Convention (CTC) member countries.

The NCTS systems of all National Administrations are connected to each other by a central domain in Brussels, so the details and progress of a transit movement can be monitored by all interested parties at every stage.

The main objectives of the NCTS are to:

- increase the efficiency and effectiveness of transit procedures
- improve the prevention and detection of fraud
- accelerate transactions carried out under a transit procedure and to offer security for them

To use the NCTS, traders need the facility to send and receive electronic messages to and from the UK NCTS. Connected traders receive electronic responses advising of key decisions during both departure and destination, such as:

- acceptance of declaration
- release of goods
- notification of discharge of liability, that is, the release of the guarantee that is in place throughout the lifespan of the movement to cover the duties at risk during the movement of goods

Traders cannot interface directly with the NCTS to input or amend data or to access records and reference data. Instead, they exchange defined structured messages with the system. 

In certain circumstances, where Simplified NCTS Procedures are used by Authorised Consignors/Consignees, processing and release will be automatic and allow, depending upon the conditions of authorisation, for ‘out-of-hours‘ clearance. This will allow for selective, risk-based controls, and for the processing of declarations and the release of goods to become largely automatic.

### Scope

This document provides an overview of the processes involved in the exchange of NCTS messages with traders and defines the messages associated with the NCTS, in particular:

- the trader’s declaration for Transit and the associated Customs response
- control and release of the movement at departure 
- the trader’s notification of arrival and the associated Customs response
- control and release of the goods at destination
- registration of any incidents that may occur during transit

These messages comply with the Functional Transit System Specification (FTSS) and Design Documentation for National Transit Application (DDNTA) documents, which are distributed by the EU Commission to National Administrations.

### NCTS reference data

The NCTS holds two types of reference data:

- common reference data:
  - stored in a central system known as Common Services Reference Data (CS/RD2)
  - applicable to all contracting parties’ NCTS systems 
  - used to validate specific fields within trader messages and ensure that they contain acceptable data

- national reference data:
  - applies locally to the systems of individual countries 
  - used to validate traders’ details, guarantee information and any authorisations they may hold when submitted in traders' messages


#### CS/RD2

Reference data within CS/RD2 comprises code lists. Each code list provides data that is used for validation against specific fields within declarations submitted by users, and also within intra-NCTS message exchange. 

The latest CS/RD2 data is released overnight on a daily basis. The most volatile code list contained in CS/RD2 is CL 141 Customs Offices, which holds details of all valid Customs Offices for all Common Transit Convention countries and all the transit functions available for each office, such as Office of Departure (DEP), Office of Destination (DES) and Office of Transit (TRA).

It is essential that any software solution developed for traders retrieves these updates on a daily basis to ensure that any validation coded into the software is synchronised with the UK NCTS to prevent unnecessary rejections.

CS/RD2 is maintained by the European Commission and you can download code lists [here](https://ec.europa.eu/taxation_customs/dds2/rd/rd_download_home.jsp?Lang=en). When downloading code lists, ensure that you select **NCTS-P5** in the **Domain** list.

#### National reference data

This is administered by each national customs administration on its own behalf. When a trader applies to use the transit procedure, specific data is captured into the NCTS, including the trader’s name and address, their EORI number, details about guarantees for transit usage that they hold and, in the case of Authorised Consignors/Consignees, details of their authorised locations and their allocated code numbers. When traders use these details in declarations, they are validated against the national reference data held by the NCTS.

### UK NCTS

The UK NCTS system comprises two separate NCTS cores, one processes Great Britain mainland transit movements while the other processes transit movements within Northern Ireland.

The two cores have different modes of operation:

- the Great Britain mainland NCTS core operates in Common Transit mode, so if a rule or condition has different applicability depending on whether the country of departure or destination or transit is within the territory of the EU or a separate CTC member country, that rule or condition will be applied to Great Britain mainland as a CTC member country
- the Northern Ireland NCTS core operates in Union Transit mode, so a territory dependent rule or condition will be applied to Northern Ireland as if it is part of EU territory.

This is an important consideration for any traders who intend to implement any rules or conditions to validate declarations for themselves or their customers.

Both cores have entirely separate common and national reference data, so they have separate country codes:

- Great Britain mainland NCTS uses **GB** as its country prefix
- Northern Ireland NCTS uses **XI** as its country prefix

The NCTS needs region-specific reference data, such as Customs Office codes, guarantee reference numbers and Economic Operator Registration and Identification (EORI) numbers (also known as the Trader Identification Numbers) to include the applicable country code.

For example:

- Dover port in Great Britain mainland has the Customs office code ‘GB000060‘
- Belfast Entry Process Unit in Northern Ireland has the Customs office code ‘XI000142‘


Additionally, authorised locations used by Authorised Consignors and Consignees exist only in the NCTS appropriate to their physical location.

Because authorised location codes are linked to the Authorised Consignor/nees’ EORI and EORIs are linked to the procedure holder’s guarantee, any software developed for the NCTS should allow use of GB EORIs and their associated GB guarantees and XI EORIs and their associated XI guarantees.

Although two separate cores are in operation, only one submission channel is used to access the UK NCTS. You can submit Great Britain mainland or Northern Ireland messages without the need to add any routing information. Your messages will be routed automatically to the correct core by a logic layer embedded in the CTC Traders API. 

#### Access to UK NCTS

Traders can use the CTC Traders API channel to exchange XML messages with both UK NCTS cores (GB and XI). This allows 3rd party developer software to use XML for message payloads when sending and receiving arrival and departure notifications.

The CTC Traders API provides:

- full Great Britain mainland and Northern Ireland integration
- a single endpoint for both Great Britain mainland and Northern Ireland declarations

### Liability amount for guarantees

Guarantee usage monitoring in the NCTS requires that a liability reference amount is recorded against each guarantee in a declaration.

Departure declarations submitted by users (IE015 message) can contain guarantee reference amounts only for guarantee types 0, 1, 2, 4 and 9. For all other guarantee types, Border Force will enter the reference amount into the NCTS manually before releasing the movement.

In exceptional circumstances, if a declarant is unable to determine the guarantee reference amount, the CTC allows the amount to be fixed at 10,000 euros for each transit operation.

If the departure declaration does not contain a guarantee reference amount and the guarantee being used is either type 0, 1, 2, 4 or 9, the system inserts 10,000 euros as the guarantee liability amount automatically.

This applies in all circumstances except for national transit movements, for example, Great Britain to Great Britain. National transit is not supported by the CTC but UK national legislation allows its usage as a trade facilitation.

### Transit Accompanying Documents

A Transit Accompanying Document (TAD) is required for each NCTS5 transit declaration.

**Note:** Transit Security Accompanying Documents (TSADs) are out of scope for NCTS5.

TADs must be created by using information only from IE029 messages.

TADs are electronically authenticated by the NCTS, so they do not need to be authenticated by the Office of Departure (OoDep) by stamp. A Common Transit (CT) movement cannot be released from transit **legally** until after the relevant IE029 message has been generated by Customs and a valid TAD has been created. 

**Note:** A TAD should be created using only data that has been validated or provided by the NCTS. This can be achieved by generating the TAD directly from the IE029 message either electronically or through printing it manually, or by using data from the relevant IE029 message to update a previously created and validated transit record, and then creating the TAD from that.

Traders using the NCTS normal procedure will have the option either to collect the TAD from the OoDep or to generate the TAD at their own premises. Approval to create the TAD is granted by the Central Community Transit Office (CCTO), to which a trader’s application must be submitted for consideration. Traders must provide evidence of their ability to create TADs in the required format.

Traders authorised to use NCTS simplified procedures as Authorised Consignors can generate their own TADs as part of their authorisation permission. 

#### Fallback procedure

For information about the TAD fallback procedure, see section 'Business continuity: ‘Unscheduled’ Downtime' of the [Transit Manual Supplement](https://www.gov.uk/government/publications/transit-manual-supplement).

#### Manually printing TADs

Guidelines for printing TADs are available in this [zip file](/guides/ctc-traders-phase5-tis/downloads/NCTS5_TAD_Printing_Guidelines_June_2023.zip):

- there are separate guidelines in the zip file for during and after the transition period (see below)
- single house consignments apply only to the transition period and multiple house consignments apply only to the post-transition period

**Note:** The current status of the post-transition period printing guidelines is ‘draft‘. If the guidelines change after they have been finalised, we will advise you.

**Note:** Please ignore any TSAD references in any of the files in the zip file.

The following printing guidelines are important:

- the ‘liability amount‘ information in the guarantee data group is not printed on a TAD
- the printer and print driver used for printing a TAD must be capable of printing a bar code of standard ISO code 128 set B (but not EAN128)
- use the font type BC C128 Narrow (True Type) version 2.0

#### Example TAD

To learn more about how to create TADs for NCTS5, review the following:

- [example transition period TAD](/guides/ctc-traders-phase5-tis/downloads/Example_NCTS5_Transition_Period_TAD_September_2023.pdf) (PDF), which is based on the NCTS4 TAD template (the TAD templates used for NCTS4 and NCTS5 transition period are the same - more information about the NCTS5 post-transition period TAD will be provided when it becomes available)
- [NCTS5 Transition Period TAD Correlation Data spreadsheet](/guides/ctc-traders-phase5-tis/downloads/NCTS5_Transition_Period_TAD_Correlation_Data_September_2023.xlsx), which maps the box numbers in an NCTS4 TAD to the corresponding data elements in NCTS5 IE013, IE015, and IE029 messages

### UK cutover from NCTS4 to NCTS5

After the UK NCTS5 service goes live (see [NCTS5 key dates](#ncts5-key-dates)), there will be a cutover period during which:

- the NCTS4 service will continue running only to deal with in-flight transit declarations submitted before the go-live date
- the NCTS5 service will handle all new transit declarations submitted from the go-live date onwards

### Transition period

The transition period (see [NCTS5 key dates](#ncts5-key-dates)) is the period of time during which countries may switch to operating NCTS5 at any point and will run until all countries have switched to operating NCTS5. NCTS operations are currently considered to be in the transition period.

During the transition period, those countries that are operating NCTS5 must do so in transitional mode, which is equivalent to a ‘backwards compatibility’ mode. This is to ensure that messages can be exchanged between NCTS4 and NCTS5 countries, which is handled by an upgrade/downgrade convertor in the common domain, where messages are exchanged at country to country level. For example, notifying the country of destination that the movement has been released or notifying the country of departure that the movement has arrived, and so on.

The UK’s NCTS5 service will go live during the transition period. 

To ensure backwards compatibility with NCTS4 during transition, special rules and conditions have been defined to restrict/prevent usage of new data fields and some functionality until all countries are operating NCTS5. This allows downgrading of NCTS5 messages to NCTS4.

The prefixes for these rules and conditions are as follows.

| Rule prefix | Description |
| ----------- | ----------- |
| B | Restrictive business rules effective during transitional period. |
| E | Restrictive technical rules effective during transitional period. |

During the transition period, NCTS will observe and apply these business ([Rules B](/guides/ctc-traders-phase5-tis/documentation/rules-b.html)) and technical ([Rules E](/guides/ctc-traders-phase5-tis/documentation/rules-e.html)) rules as defined in this document.

### Message sender and recipient guidelines

There are guidelines for entering message sender and recipient details in arrivals and departures messages in the NCTS5 Trader Test environment that will also apply to the production version of the UK NCTS5 service.

#### Message sender

When specifying the message sender of an arrival or departure message, you can enter alphanumeric format data up to 35 characters (‘an..35‘).

We recommend that you should enter the EORI number of the organisation (‘the declarant‘) that is physically sending the message. Alternatively, if you do not know the EORI number of the declarant, you can use the EORI number of the transit movement or prompt for it.

#### Message recipient

When specifying the message recipient of an arrival message for a GB to XI or XI to GB transit movement, you must enter ‘NTA‘ and the correct country code of the **actual** office of destination (either NTA.GB or NTA.XI, whichever is applicable), which could be different from the declared office of destination.

When specifying the message recipient of a departure message for a GB to XI or XI to GB transit movement, you must enter ‘NTA‘ and the correct country code of the office of departure (either NTA.GB or NTA.XI, whichever is applicable).

If any of your transit movements involve other CTC member countries, you must enter NTA and any other information advised by each member country in its NCTS5 documentation. Please note that the rules used by other CTC members for message recipient might be different from those used by the UK.

For more information entering message recipient details in messages for GB to XI or XI to GB transit movements, see [CTC Traders API phase 5 testing guide](/guides/ctc-traders-phase5-testing-guide/documentation/test-scenarios.html#message-recipient).

### Date-time format

NCTS5 uses the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard for timestamps. If the optional timezone data is omitted from the timestamp of a message sent to the NCTS, [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) is used for any responses.

### Important NCTS5 terms

The following terms are important to understand in NCTS5:

- **Consignment:** The header information is provided and applies to the whole transit declaration (up to 1 Consignment level per declaration).
- **House consignment:** The lowest transport information is provided, and this applies to all its Consignment Items (each Consignment can contain up to 99 House Consignments).

    The House Consignment level covers information relating to all goods that are subject to the same house transport contract. A house transport contract is a transport contract with a freight forwarder, non-vessel or aircraft operating common carrier or its agent or a postal operator. Where several house transport contracts exist, the information provided in customs declarations, notifications and proof of the customs status as Union Goods should relate to the lowest level of contracts. This is usually the contract concluded by a freight forwarder and the shipper.

    The new House Consignment level is introduced to give more flexibility to the Economic Operators, allowing them to lodge one declaration with several Consignors/Consignees.

- **Consignment item:** The items information is provided (each House Consignment can contain up to 999 Consignment Items).

## Changelog

You can find the changelog in the [ctc-traders-phase5-tis](https://github.com/hmrc/ctc-traders-phase5-tis/wiki/NCTS-Phase-5-Technical-Interface-Specification-(TIS)-changelog) GitHub wiki.
