---
title: NCTS Phase 5 Technical Interface Specification
weight: 5
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---
# Message types

## Accessing the XML Schemas

The XML schemas are available for download [here](https://github.com/hmrc/transit-movements-validator/tree/main/conf/xsd).

You can view the XML schema for a particular message type as follows:

1. Navigate to the required message type listed in this section.
1. Under the **XML Root** heading in the table, click the link. 
    
    The selected XML schema is displayed in GitHub.

## IE004 Amendment Acceptance
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE004
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc004c.xsd">
    CC004C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    AMENDMENT ACCEPTANCE
   </p>
  </td>
  <td style="">
   E_AMD_ACC
  </td>
 </tr>
</table>


## IE007 Arrival Notification

<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE007
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc007c.xsd">
    CC007C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    ARRIVAL NOTIFICATION
   </p>
  </td>
  <td style="">
   E_ARR_NOT
  </td>
 </tr>
</table>

## IE009 Invalidation Decision
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE009
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc009c.xsd">
    CC009C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    INVALIDATION DECISION
   </p>
  </td>
  <td style="">
   E_INV_DEC
  </td>
 </tr>
</table>

## IE013 Declaration Amendment
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE013
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc013c.xsd">
    CC013C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    DECLARATION AMENDMENT
   </p>
  </td>
  <td style="">
   E_DEC_AMD
  </td>
 </tr>
</table>

## IE014 Declaration Invalidation Request
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE014
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc014c.xsd">
    CC014C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    DECLARATION INVALIDATION REQUEST
   </p>
  </td>
  <td style="">
   E_DEC_INV
  </td>
 </tr>
</table>

## IE015 Declaration Data
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE015
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc015c.xsd">
    CC015C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    DECLARATION DATA
   </p>
  </td>
  <td style="">
   E_DEC_DAT
  </td>
 </tr>
</table>

## IE019 Discrepancies
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE019
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc019c.xsd">
    CC019C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    DISCREPANCIES
   </p>
  </td>
  <td style="">
   E_DIS_SND
  </td>
 </tr>
</table>

## IE025 Goods Release Notification
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE025
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc025c.xsd">
    CC025C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    GOODS RELEASE NOTIFICATION
   </p>
  </td>
  <td style="">
   E_GDS_REL
  </td>
 </tr>
</table>

## IE028 MRN Allocated
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE028
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc028c.xsd">
    CC028C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    MRN ALLOCATED
   </p>
  </td>
  <td style="">
   E_MRN_ALL
  </td>
 </tr>
</table>

## IE029 Release for Transit
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE029
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc029c.xsd">
    CC029C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    RELEASE FOR TRANSIT
   </p>
  </td>
  <td style="">
   E_REL_TRA
  </td>
 </tr>
</table>

## IE035 Recovery Notification
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE035
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc035c.xsd">
    CC035C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    RECOVERY NOTIFICATION
   </p>
  </td>
  <td style="">
   E_REC_NOT
  </td>
 </tr>
</table>

## IE043 Unloading Permission
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE043
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc043c.xsd">
    CC043C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    UNLOADING PERMISSION
   </p>
  </td>
  <td style="">
   E_ULD_PER
  </td>
 </tr>
</table>

## IE044 Unloading Remarks
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE044
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc044c.xsd">
    CC044C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    UNLOADING REMARKS
   </p>
  </td>
  <td style="">
   E_ULD_REM
  </td>
 </tr>
</table>

## IE045 Write-Off Notification
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE045
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc045c.xsd">
    CC045C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    WRITE-OFF NOTIFICATION
   </p>
  </td>
  <td style="">
   E_WRT_NOT
  </td>
 </tr>
</table>

## IE051 No Release for Transit
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE051
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc051c.xsd">
    CC051C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    NO RELEASE FOR TRANSIT
   </p>
  </td>
  <td style="">
   E_REL_NOT
  </td>
 </tr>
</table>

## IE055 Guarantee Not Valid
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE055
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc055c.xsd">
    CC055C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    GUARANTEE NOT VALID
   </p>
  </td>
  <td style="">
   E_GUA_INV
  </td>
 </tr>
</table>

## IE056 Rejection from Office of Departure
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:24pt">
  <td style="">
   <p class="s3" style="">
    IE056
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc056c.xsd">
    CC056C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    REJECTION FROM OFFICE OF DEPARTURE
   </p>
  </td>
  <td style="">
   E_DEP_REJ
  </td>
 </tr>
</table>

## IE057 Rejection from Office of Destination
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:24pt">
  <td style="">
   <p class="s3" style="">
    IE057
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc057c.xsd">
    CC057C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    REJECTION FROM OFFICE OF DESTINATION
   </p>
  </td>
  <td style="">
   E_DES_REJ
  </td>
 </tr>
</table>

## IE060 Control Decision Notification
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE060
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc060c.xsd">
    CC060C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    CONTROL DECISION NOTIFICATION
   </p>
  </td>
  <td style="">
   E_CTR_DEC
  </td>
 </tr>
</table>

## IE170 Presentation Notification for the Pre-Lodged Declaration
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:24pt">
  <td style="">
   <p class="s3" style="">
    IE170
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc170c.xsd">
    CC170C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    PRESENTATION NOTIFICATION FOR THE PRE-LODGED DECLARATION
   </p>
  </td>
  <td style="">
   E_PRE_NOT
  </td>
 </tr>
</table>

## IE182 Forwarded Incident Notification To ED
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:24pt">
  <td style="">
   <p class="s3" style="">
    IE182
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc182c.xsd">
    CC182C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    FORWARDED INCIDENT NOTIFICATION TO ED
   </p>
  </td>
  <td style="">
   E_INC_NOT
  </td>
 </tr>
</table>

## IE928 Positive Acknowledge
<table cellspacing="0" style="border-collapse:collapse;margin-left:6pt">
 <tr>
  <th>
   Message Type
  </th>
  <th>
   XML Root
  </th>
  <th>
   Name
  </th>
  <th>
   Short Name
  </th>
 </tr>
 <tr style="height:14pt">
  <td style="">
   <p class="s3" style="">
    IE928
   </p>
  </td>
  <td style="">
   <a href="https://github.com/hmrc/transit-movements-validator/blob/main/conf/xsd/cc928c.xsd">
    CC928C
   </a>
  </td>
  <td style="">
   <p class="s3" style="">
    POSITIVE ACKNOWLEDGE
   </p>
  </td>
  <td style="">
   E_POS_ACK
  </td>
 </tr>
</table>