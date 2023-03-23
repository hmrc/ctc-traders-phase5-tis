## Message details

Message type details are as follows: 

- characteristics of the data groups belonging to a message: sequence, number of repetitions, and a status value to indicate if a data group is one of the folllowing: 
    - mandatory ('R': Required)
    - optional ('O': Optional) 
    - conditional ('D': Dependent)
- characteristics of the data items belonging to a data group: sequence, number of repetitions, type, length, and a value to indicate if a data item is one of the folllowing: 
    - mandatory ('R': Required) 
    - optional ('O': Optional)
    - conditional ('D': Dependent)
- data group nesting is shown with dashes, which means that a data group may contain not only data items but also other groups of data. 
- links to applicable NCTS code lists:
    - each link downloads a zip file from a European Commission [website](https://ec.europa.eu/taxation_customs/dds2/rd/rd_download_home.jsp?Lang=en)
    - the code lists are updated regularly
    - consider setting up an automated way to download the files regularly and integrate them with your software
- links to applicable rules and conditions 
- header elements (XML fields that can contain other XML fields) are highlighted in **bold**

## Message categorisation by sender

Some message types are sent by the NCTS while other message types are sent by traders.

**Note:** The 'Status' column in each table indicates whether a message type is new in NCTS phase 5, or new to the United Kingdom (UK) in phase 5, or upgraded from phase 4 to phase 5.

### Messages from the NCTS

| Code  | Message | Status |
| ----- | ------- | ------ |
| IE004 | Amendment Acceptance | New to UK in phase 5 |
| IE009 | Invalidation Decision | Phase 4 to phase 5 upgrade |
| IE019 | Discrepancies | New to UK in phase 5 |
| IE022 | Notification To Amend Declaration | New in phase 5 (out of scope until after 30 November 2023) |
| IE025 | Goods Release Notification | Phase 4 to phase 5 upgrade |
| IE028 | MRN Allocated | Phase 4 to phase 5 upgrade |
| IE029 | Release For Transit | Phase 4 to phase 5 upgrade |
| IE035 | Recovery Notification | New to UK in phase 5 |
| IE043 | Unloading Permission | Phase 4 to phase 5 upgrade |
| IE045 | Write-Off Notification | Phase 4 to phase 5 upgrade |
| IE051 | No Release For Transit | Phase 4 to phase 5 upgrade |
| IE055 | Guarantee Not Valid | Phase 4 to phase 5 upgrade |
| IE056 | Rejection From Office Of Departure    | New in phase 5 |
| IE057 | Rejection From Office Of Destination  | New in phase 5 |
| IE060 | Control Decision Notification | Phase 4 to phase 5 upgrade |
| IE182 | Forwarded Incident Notification To ED | New in phase 5 |
| IE928 | Positive Acknowledge | Phase 4 to phase 5 upgrade |

### Messages from traders

| Code  | Message | Status |
| ----- | ------- | ------ |
| IE007 | Arrival Notification | Phase 4 to phase 5 upgrade |
| IE013 | Declaration Amendment | New to UK in phase 5 |
| IE014 | Declaration Invalidation Request | Phase 4 to phase 5 upgrade |
| IE015 | Declaration Data | Phase 4 to phase 5 upgrade |
| IE044 | Unloading Remarks | Phase 4 to phase 5 upgrade |
| IE170 | Presentation Notification For The Pre-Lodged Declaration | New in phase 5 |

## Accessing the XML schemas

The XML schemas are available on [GitHub](https://github.com/hmrc/transit-movements-validator/tree/main/conf/xsd).

You can view the XML schema for a particular message type as follows:

1. Navigate to the required message type listed in this section.
2. Under the **XML Root** heading in the table, click the link. 
   
    The selected XML schema is displayed in GitHub.

