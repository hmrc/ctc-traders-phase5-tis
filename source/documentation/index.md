---
title: NCTS Phase 5 Technical Interface Specification
weight: 1
description: Software developers, designers, product owners or business analysts. Integrate your software with the ERMIS service
---

# NCTS Phase 5 Technical Interface Specification

Version 0.0.1a issued April 2022
***


## Overview

Some stuff here about the TIS and CTC and NCTS/ERMIS?

## Important phase 5 terms

The following terms are important to understand in phase 5:

- **Consignment:** The header information is provided and applies to the whole transit declaration (up to 1 Consignment level per declaration).

- **House Consignment:** The lowest transport information is provided, and this applies to all its Consignment Items (each Consignment can contain up to 99 House Consignments).

    The House Consignment level covers information relating to all goods that are subject to the same house transport contract. A house transport contract is a transport contract with a freight forwarder, non-vessel or aircraft operating common carrier or his agent or a postal operator. Where several house transport contracts exist, the information provided in customs declarations, notifications and proof of the customs status as Union Goods should relate to the lowest level of contracts. This is usually the contract concluded by a freight forwarder and the shipper.

    The new House Consignment level is introduced to give more flexibility to the Economic Operators, allowing them to lodge one declaration with several Consignors/Consignees.

- **Consignment Item:** The items information is provided (each House Consignment can contain up to 999 Consignment Items).

## Pre-lodgement message flows

### Transit presentation notification valid (DDNTA section: III.II.2.1.1)

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



### Transit presentation not valid (DDNTA section: III.II.2.1.3)

**Applicable procedures:** normal and simplified.

<img src="figures/trans_pres_notif_not_valid.svg" alt="Pre-lodgement message flow with presentation of a non-valid notification. Flow is described in this section." />

<a href="figures/trans_pres_notif_not_valid.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the Office of Departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The Office of Departure validates this message successfully and sends the ‘Positive Acknowledge’ E_POS_ACK (IE928) message to the Holder of the Transit Procedure to acknowledge receipt of the transit declaration.
1. The Office of Departure receives an invalid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message from the Holder of the Transit Procedure.
1. The Office of Departure rejects the E_PRE_NOT (IE170) message by notifying the Holder of the Transit Procedure with the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message.
1. If the time limit expires without the Holder of the Transit Procedure resending a valid ‘Presentation Notification for the Pre-Lodged Declaration’ E_PRE_NOT (IE170) message, the Holder of the Transit Procedure is notified with the message ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) by the Office of Departure.
1. The transit movement ends.



### Corrections of the pre-lodgement declaration prior to presentation of the goods (DDNTA section: III.II.2.1.2)

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




### Cancellation of the pre-lodged declaration (DDNTA section: III.II.2.1.4)

**Applicable procedures:** normal and simplified.

<img src="figures/cancel_pre-lodge_dec.svg" alt="Pre-lodgement message flow with cancellation of the pre-lodgement declaration. Flow is described in this section." />

<a href="figures/cancel_pre-lodge_dec.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits the ‘Declaration Data’ E_DEC_DAT (IE015) message to the Office of Departure with ‘Additional Declaration Type’ equal to ‘D’.
1. The Office of Departure validates this message successfully and sends the ‘Positive Acknowledge’ E_POS_ACK (IE928) message to the Holder of the Transit Procedure to acknowledge receipt of the transit declaration.
1. The Holder of the Transit Procedure decides to cancel the pre-lodged declaration by sending the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message to the Office of Departure.
1. Assuming the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message is valid, the Office of Departure automatically sends a positive decision to cancel the pre-lodged declaration. The ‘Invalidation Decision’ E_INV_DEC (IE009) is sent to the Holder of the Transit Procedure.
1. The transit movement ends.







## Departure message flows

### Standard departure (DDNTA section: III.II.1.1)

**Applicable procedures:** normal and simplified.

<img src="figures/standard_departure.svg" alt="Standard departure message flow. Flow is described in this section." />

<a href="figures/standard_departure.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits a transit declaration to the Office of Departure with the ‘Declaration Data’ E_DEC_DAT (IE015) message.
1. If the transit declaration is valid, the Office of Departure acknowledges the receipt of the transit declaration with the ‘Positive Acknowledge’ E_POS_ACK (IE928) message.
1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.




### Rejection of transit declaration (DDNTA section: III.II.2.3)

**Applicable procedures:** normal and simplified.

<img src="figures/reject_transit_declaration.svg" alt="Rejection of transit declaration. Flow is described in this section." />

<a href="figures/reject_transit_declaration.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Holder of the Transit Procedure submits a transit declaration to the Office of Departure with the ‘Declaration Data’ E_DEC_DAT (IE015) message.
2. The Office of Departure validates the declaration data as invalid and thus rejects it by sending a response to the Holder of the Transit Procedure the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message.
3. The transit movement ends.





### Release for transit refused due to guarantee registration failure (DDNTA section: III.II.2.9.2)

**Applicable procedures:** normal and simplified.

<img src="figures/guarantee_registration_failure.svg" alt="Release for transit refused due to guarantee registration failure. Flow is described in this section." />

<a href="figures/guarantee_registration_failure.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Holder of the Transit Procedure is notified that the declared guarantee is not valid with the ‘Guarantee Not Valid’ E_GUA_INV (IE055) message.
1. The Holder of the Transit Procedure does not send a ‘Declaration Amendment’ E_DEC_AMD (IE013) within the allowed time period. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the Holder of the Transit Procedure.
1. The transit movement ends.






### Release for transit refused for safety and security reasons (DDNTA section: III.II.2.9.3)


**Applicable procedures:** normal and simplified.

<img src="figures/release_refused_safety_security.svg" alt="Release for transit refused for safety and security reasons. Flow is described in this section." />

<a href="figures/release_refused_safety_security.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. A risk assessment of the transit declaration identifies a high risk with a threat to safety and security. The ‘No Release for Transit’ E_REL_NOT (IE051) message is sent to the Holder of the Transit Procedure.
1. The transit movement ends.




### Declaration amendment accepted/rejected (DDNTA section: III.II.2.4.1 & III.II.2.4.2)

**Applicable procedures:** normal and simplified.

<img src="figures/amendment_accepted_rejected.svg" alt="Declaration amendment accepted/rejected. Flow is described in this section." />

<a href="figures/amendment_accepted_rejected.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Holder of the Transit Procedure notifies the Office of Departure of needed changes to the original declaration with a valid ‘Declaration Amendment’ E_DEC_AMD (IE013) before the goods have been released for transit.
1. The Office of Departure performs validation of the IE013 message with one of the following outcomes:
    - The Office of Departure sends the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) to the Holder of the Transit Procedure, who can then send a second ‘Declaration Amendment’ E_DEC_AMD (IE013) message for validation. (Go to step 5.)
    - The Office of Departure successfully validates the IE013 message and sends its acceptance to the Holder of the Transit Procedure with the ‘Amendment Acceptance’ E_AMD_ACC (IE004) message. (Go to step 6.)
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The movement continues to arrivals.



### Invalidation request by the holder of the transit procedure before release for transit (DDNTA section: III.II.2.10.1)

**Applicable procedures:** normal and simplified.

<img src="figures/inval_request_before_release.svg" alt="Invalidation request by the holder of the transit procedure before release for transit. Flow is described in this section." />

<a href="figures/inval_request_before_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The Holder of the Transit Procedure is notified with the ‘Guarantee Not Valid’ E_GUA_INV (IE055) message that the declared guarantee is not valid.
1. The Holder of the Transit Procedure decides to invalidate the transit declaration and therefore notifies the Office of Departure with the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message.
1. The Office of Departure examines the request and replies with the positive decision with the ‘Invalidation Decision’ E_INV_DEC (IE009) message (i.e. “Decision” is set to “1=Yes”).
1. The transit movement ends.





### Invalidation request by the holder of the transit procedure after release for transit (DDNTA section: III.II.2.10.2)

**Applicable procedures:** normal and simplified.

<img src="figures/inval_request_after_release.svg" alt="Invalidation request by the holder of the transit procedure after release for transit. Flow is described in this section." />

<a href="figures/inval_request_after_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The Holder of the Transit Procedure decides to invalidate the transit declaration and therefore notifies the Office of Departure with the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) message.
1. The Office of Departure automatically rejects the ‘Declaration Invalidation Request’ E_DEC_INV (IE014) by notifying the Holder of the Transit Procedure with the ‘Rejection from Office of Departure’ E_DEP_REJ (IE056) message containing the error code ’92-Message out of sequence’.
1. The movement continues to arrivals.




### Invalidation of a transit declaration after release for transit (DDNTA section: III.II.2.10.4) 

**Applicable procedures:** normal and simplified.

<img src="figures/inval_declar_after_release.svg" alt="Invalidation of a transit declaration after release for transit. Flow is described in this section." />

<a href="figures/inval_declar_after_release.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Office of Departure communicates the MRN to the Holder of the Transit Procedure with the ‘MRN Allocated’ E_MRN_ALL (IE028) message.
1. The ‘Release for Transit’ E_REL_TRA (IE029) message is sent to the Holder of the Transit Procedure.
1. The ‘Invalidation Decision’ E_INV_DEC (IE009) is sent to the Holder of the Transit Procedure.
1. The transit movement ends.





### Control by Office of Departure with release for transit (DDNTA section: III.II.2.5)

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




### Positive release request with release for transit / negative release request (DDNTA section: III.II.2.6.1 & III.II.2.6.2 )

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





### Release request rejected (DDNTA section: III.II.2.6.3) 

**Applicable procedures:** normal and simplified.

<img src="figures/release_request_rejected.svg" alt="Positive release request with release for transit / negative release request. Flow is described in this section." />

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

### Standard procedure at destination (DDNTA section: III.II.1.1)

**Applicable procedures:** normal and simplified.

<img src="figures/standard_arrival.svg" alt="Standard arrival message flow. Flow is described in this section." />

<a href="figures/standard_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message.
1. The goods are released from transit. The Office of Destination sends the ‘Goods Released Notification’ E_GDS_REL (IE025) message to the Trader at Destination.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.




### Simplified procedure at destination (DDNTA section: III.II.4.2)

**Applicable procedures:** simplified.

<img src="figures/simplified_arrival.svg" alt="Simplified arrival message flow. Flow is described in this section." />

<a href="figures/simplified_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. Upon arrival of the movement at the Office of Destination, the Trader at Destination announces it by submitting the ‘Arrival Notification’ E_ARR_NOT (IE007) message under simplified procedure (simplified procedure flag = ‘Yes’).
1. The Office of Destination notifies the Trader at Destination that the unloading of the goods can be started by means of ‘Unloading Permission’ E_ULD_PER (IE043).
1. After unloading, the Trader at Destination sends the ‘Unloading Remarks’ E_ULD_REM (IE044) to the Office of Destination indicating that the unloading has been completed with no unloading remarks (i.e. the ‘Unloading Remarks’ E_ULD_REM (IE044) message contains the flags Unloading completion = ‘1-Yes’ & Conform = ‘1-Yes’).
1. The goods are released from transit. The Office of Destination sends the ‘Goods Released Notification’ E_GDS_REL (IE025) message to the Trader at Destination.
1. The Office of Departure sends the ‘Write-Off Notification’ E_WRT_NOT (IE045) message to the Holder of the Transit Procedure.



### Rejection of arrival notification (DDNTA section: III.II.4.6)

<img src="figures/reject_arrival.svg" alt="Rejection of arrival notification. Flow is described in this section." />

<a href="figures/reject_arrival.svg" target="_blank">Open the diagram in a new tab.</a>

1. The Trader at Destination sends the ‘Arrival Notification’ E_ARR_NOT (IE007) to the Office of Destination and NCTS performs validation of this message. If the ‘Arrival Notification’ E_ARR_NOT (IE007) has been found invalid after validation (i.e. in terms of message structure and R/Cs), NCTS rejects it.
1. The Office of Destination notifies the Trader at Destination by sending the ‘Rejection from Office of Destination’ E_DES_REJ (IE057) message.
1. The Trader at Destination sends another ‘Arrival Notification’ E_ARR_NOT (IE007) to the Office of Destination and NCTS performs validation of this message. This time, the ‘Arrival Notification’ E_ARR_NOT (IE007) has been found valid after validation (i.e. in terms of message structure and R/Cs), NCTS accepts it.



### Unloading Permission Received - Unloading Remarks (DDNTA section: III.II.4.4 )

**Applicable procedures:** simplified.

<img src="figures/unload_perm_rec_remarks.svg" alt="Unloading Permission Received - Unloading Remarks. Flow is described in this section." />

<a href="figures/unload_perm_rec_remarks.svg" target="_blank">Open the diagram in a new tab.</a>



## Other message flows