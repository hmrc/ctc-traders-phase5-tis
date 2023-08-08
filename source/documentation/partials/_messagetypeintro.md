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

## NCTS error codes

The following error codes can be returned by the NCTS.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 68%" />
<col style="width: 13%" />
</colgroup>
<thead>
<th>Value</th>
<th>Description</th>
<th>Explanation</th>
<th>Transition period applicablility</th>
</tr>
</thead>
<tbody>
<td>12</td>
<td>Codelist violation</td>
<td><p>The value of a data item is outside the predefined set of values, that is, not part of the applicable business or technical codelist.</p>
<p>Example: The data element with CL027 (‘0’ or ‘1’) includes the value ‘2’. It violates the CL027.</p></td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<tr class="even">
<td>13</td>
<td>Condition violation (missing)</td>
<td><p>A condition (Cxxxx or Txxxx) is violated due to missing data group or data item is missing (while "R").</p>
<p>Example: Violation of C0569 - Declared number of seals is "2" and no seals are declared.</p>
<p><em>(IF /<span>&#42;</span>/GoodsShipment/Consignment/TransportEquipment/numberOfSeals is GREATER than "0"</em></p>
<p><em>THEN /<span>&#42;</span>/GoodsShipment/Consignment/TransportEquipment/Seal = "R"</em></p>
<p><em>ELSE /<span>&#42;</span>/GoodsShipment/Consignment/TransportEquipment/Seal = "N".)</em></p></td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<td>14</td>
<td>Rule violation</td>
<td><p>A rule (Rxxxx or Txxxx) is violated and consequently a data group or a data item includes an invalid value.</p>
<p>Example: Violation of R0007 - The first declared Goods item number is 2.</p>
<p>(Each &lt;GOODS SHIPMENT - GOODS ITEM.Goods item number&gt; is unique throughout the declaration. The items shall be numbered in a sequential fashion, starting from "1" for the first item and incrementing the numbering by "1" for each following item.)</em></p></td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<td>15</td>
<td>Condition violation (not allowed)</td>
<td><p>A condition (Cxxxx or Txxxx) is violated and consequently a data group or data item is present despite it shall not be present (it is present while "N").</p>
<p>Example: Violation of C0569 - Declared number of seals is ‘0’ and seals are declared.</p>
<p><em>(IF /<span>&#42;</span>/GoodsShipment/Consignment/TransportEquipment/numberOfSeals is GREATER than "0"</em></p>
<p><em>THEN /<span>&#42;</span>/GoodsShipment/Consignment/TransportEquipment/Seal = "R"</em></p>
<p><em>ELSE /<span>&#42;</span>/GoodsShipment/Consignment/TransportEquipment/Seal = "N")</em></p></td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<td>26</td>
<td>Duplicate Message ID</td>
<td>The message includes the same 'Message identifier' as another message already received and processed.</td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<td>50</td>
<td>Transitional constraint Violation</td>
<td><p>A transitional constraint (Exxxx or Bxxxx) is violated. A data group is missing or too many repetitions are in the message. A data item is missing or is present despite it may not be present, or a data item includes an incorrect value (including violation of the format).</p>
<p>Example: Violation of E1108 – Declaration with 10.000.000 packages.</p>
<p><em>(IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;</em></p>
<p><em>THEN /<span>&#42;</span>/ExportOperation/totalNumberOfPackages</em></p>
<p><em>format shall be set to n..7)</em></p></td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<td>51</td>
<td>EDI violation post downgrade</td>
<td>After the 'downgrade' conversion (from 'Legacy' to 'To Be') the EDIFACT message is syntactically incorrect (a CD906C is generated and sent back to the application that initiated the conversion).</td>
<td><ul>
<li><p>During</p></li>
</ul></td>
</tr>
<td>52</td>
<td>Functional violation post downgrade</td>
<td><p>After the 'downgrade' conversion (from 'Legacy' to 'To Be') the EDIFACT message is semantically incorrect:</p>
<ul>
<li><p>FMS (sequencing, optionalities, repetitions, formatting) is violated</p></li>
<li><p>Business Validation (Rxxx, Cxxx or TRxxxx and Codelist validation) is violated</p></li>
</ul></td>
<td><ul>
<li><p>During</p></li>
</ul></td>
</tr>
<td>90</td>
<td>Unknown MRN</td>
<td><p>A message is received with MRN unknown to the destination (exception is the IEx01 messages concerning movement creation). To be used only when there is no ‘negative response’.</p>
<p>Example: The CDx02C is received and MRN is unknown, it must be responded with negative CDx03C; not with CD906C.</p>
<p>But: If a message CD115C is received and MRN is unknown, it must be responded with a CD906C with code "90".</p></td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<td>92</td>
<td>Message out of sequence</td>
<td><p>The message cannot be processed, because the receiver’s states machine is not in the state that does not allow to process the received message.</p>
<p>Example: The NTA (office of departure) receives the message CD018C while the movement is still in the state 'Under control'.</p></td>
<td><ul>
<li><p>During</p></li>
<li><p>After</p></li>
</ul></td>
</tr>
<td>93</td>
<td>Invalid MRN</td>
<td><p>The message includes a value for the data item &lt;MRN&gt; that violates the structure defined in the DDCOM.</p>
<p>Example: The ‘Check digit’ is not valid.</p></td>
<td><ul>
<li><p>During</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Accessing the XML schemas

The XML schemas are available on [GitHub](https://github.com/hmrc/transit-movements-validator/tree/main/conf/xsd).

You can view the XML schema for a particular message type as follows:

1. Navigate to the required message type listed in this section.
2. Under the **XML Root** heading in the table, click the link. 
   
    The selected XML schema is displayed in GitHub.

