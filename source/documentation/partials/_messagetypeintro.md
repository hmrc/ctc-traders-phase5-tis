## Message details

Message type details are as follows: 

- characteristics of the data groups belonging to a message: sequence, number of repetitions, and a status value to indicate if a data group is one of the folllowing: 
    - mandatory ('R': Required)
    - optional ('O': Optional) 
    - conditional ('D': Dependent)
    - do not use ('N': Not Usable)
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

**Note:** If you use a data group with priority 'N' in a message, NCTS will reject the message. 

## Message categorisation by sender

Some message types are sent by the NCTS while other message types are sent by traders.

**Note:** The 'Status' column in each table indicates whether a message type is new in NCTS5, or new to the United Kingdom (UK) in NCTS5, or upgraded from NCTS4 to NCTS5.

### Messages from the NCTS

| Code  | Message | Status |
| ----- | ------- | ------ |
| IE004 | Amendment Acceptance | New to UK in NCTS5 |
| IE009 | Invalidation Decision | NCTS4 to NCTS5 upgrade |
| IE019 | Discrepancies | New to UK in NCTS5 |
| IE022 | Notification To Amend Declaration | New in NCTS5 (out of scope until after 2 December 2024) |
| IE025 | Goods Release Notification | NCTS4 to NCTS5 upgrade |
| IE028 | MRN Allocated | NCTS4 to NCTS5 upgrade |
| IE029 | Release For Transit | NCTS4 to NCTS5 upgrade |
| IE035 | Recovery Notification | New to UK in NCTS5 |
| IE043 | Unloading Permission | NCTS4 to NCTS5 upgrade |
| IE045 | Write-Off Notification | NCTS4 to NCTS5 upgrade |
| IE051 | No Release For Transit | NCTS4 to NCTS5 upgrade |
| IE055 | Guarantee Not Valid | NCTS4 to NCTS5 upgrade |
| IE056 | Rejection From Office Of Departure    | New in NCTS5 |
| IE057 | Rejection From Office Of Destination  | New in NCTS5 |
| IE060 | Control Decision Notification | NCTS4 to NCTS5 upgrade |
| IE182 | Forwarded Incident Notification To ED | New in NCTS5 |
| IE928 | Positive Acknowledge | NCTS4 to NCTS5 upgrade |

### Messages from traders

| Code  | Message | Status |
| ----- | ------- | ------ |
| IE007 | Arrival Notification | NCTS4 to NCTS5 upgrade |
| IE013 | Declaration Amendment | New to UK in NCTS5 |
| IE014 | Declaration Invalidation Request | NCTS4 to NCTS5 upgrade |
| IE015 | Declaration Data | NCTS4 to NCTS5 upgrade |
| IE044 | Unloading Remarks | NCTS4 to NCTS5 upgrade |
| IE170 | Presentation Notification For The Pre-Lodged Declaration | New in NCTS5 |

## Accessing the XML schemas

The XML schemas are available on [GitHub](https://github.com/hmrc/transit-movements-validator/tree/main/conf/v2_1/xsd).

You can view the XML schema for a particular message type as follows:

1. Navigate to the required message type listed in this section.
2. Under the **XML Root** heading in the table, click the link. 
   
    The selected XML schema is displayed in GitHub.

