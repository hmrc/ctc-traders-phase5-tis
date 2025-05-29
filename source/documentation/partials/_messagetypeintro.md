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

### Messages from the NCTS

| Code  | Message                               |
|-------|---------------------------------------|
| IE004 | Amendment Acceptance                  |
| IE009 | Invalidation Decision                 |
| IE019 | Discrepancies                         |
| IE022 | Notification To Amend Declaration     |
| IE025 | Goods Release Notification            |
| IE028 | MRN Allocated                         |
| IE029 | Release For Transit                   |
| IE035 | Recovery Notification                 |
| IE043 | Unloading Permission                  |
| IE045 | Write-Off Notification                |
| IE051 | No Release For Transit                |
| IE055 | Guarantee Not Valid                   |
| IE056 | Rejection From Office Of Departure    |
| IE057 | Rejection From Office Of Destination  |
| IE060 | Control Decision Notification         |
| IE182 | Forwarded Incident Notification To ED |
| IE928 | Positive Acknowledge                  |

### Messages from traders

| Code  | Message                                                  |
|-------|----------------------------------------------------------|
| IE007 | Arrival Notification                                     |
| IE013 | Declaration Amendment                                    |
| IE014 | Declaration Invalidation Request                         |
| IE015 | Declaration Data                                         |
| IE044 | Unloading Remarks                                        |
| IE170 | Presentation Notification For The Pre-Lodged Declaration |

## Accessing the XML schemas

The XML schemas are available on [GitHub](https://github.com/hmrc/transit-movements-validator/tree/main/conf/v2_1/xsd).

You can view the XML schema for a particular message type as follows:

1. Navigate to the required message type listed in this section.
2. Under the **XML Root** heading in the table, click the link. 
   
    The selected XML schema is displayed in GitHub.

