---
title: List of rules
weight: 999
description: Software developers, designers, product owners or business analysts. Integrate your software with the Income Tax API for Making Tax Digital.
---
#List of rules

##RULE B1000
<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt; THEN
            This D.G. can be also used
            - in case of Export followed by transit (maximum one MRN included per one Consignment item)
            AND
            - if the &lt;TRANSIT OPERATION.Additional Declaration Type&gt; is EQUAL to 'A'.
  </td>
</tr>


</table>
## RULE B1831

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN C0598 shall be disabled AND
            IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3} AND
            the first two characters of the /*/CustomsOfficeOfTransitDeclared/referenceNumber is in SET CL010
            AND the first two characters of
            /*/CustomsOfficeOfDeparture/referenceNumber is NOT in SET CL010
            THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; = "R"
            ELSE &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; = "O"
  </td>
</tr>


</table>
## RULE B1848

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN C0586 attached to /*/Consignment/CountryOfRoutingOfConsignment shall be disabled AND
            IF /*/Transit Operation/security is in SET {1, 2, 3}
            THEN /*/Consignment/CountryOfRoutingOfConsignment = "R"
            ELSE /*/Consignment/CountryOfRoutingOfConsignment = "N"
  </td>
</tr>


</table>
## RULE B1895

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN C0502 shall be disabled AND
            IF /*/Consignment/referenceNumberUCR is PRESENT
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "N"
            ELSE
            /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "O"
  </td>
</tr>


</table>
## RULE B1896

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt; AND
            /*/TransitOperation/security is in SET {1, 3}
            THEN
            IF /*/Consignment/referenceNumberUCR is NOT PRESENT AND
            /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR IS NOT PRESENT
            THEN /*/Consignment/TransportDocument = ''R''
            ELSE /*/Consignment/TransportDocument = ''O''
  </td>
</tr>


</table>
## RULE B2400

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;
            THEN /*/Consignment/Incident = "N";

            IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;
            THEN /*/Enquiry/returnCopyReturnedDate = "N"
  </td>
</tr>


</table>
## RULE E1102

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt; THEN
            /*/HolderOfTheTransitProcedure/Address/postcode AND
            /*/Consignment/Consignor/Address/postcode AND
            /*/Consignment/Consignee/Address/postcode AND
            /*/Consignment/LocationOfGoods/Address/postcode AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/postcode AND
            /*/Consignment/ConsigneeActual/Address/postcode AND
            /*/GuaranteeReference/Guarantor/Address/postcode

            format shall be set to an..9
  </td>
</tr>


</table>
## RULE E1103

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt; THEN
            /*/Consignment/ActiveBorderTransportMeans/identificationNumber AND
            /*/Consignment/DepartureTransportMeans/identificationNumber AND
            /CD038C/Consignment/Incident/Transhipment/TransportMeans/ identificationNumber

            format shall be set to an..27
  </td>
</tr>


</table>
## RULE E1104

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/HolderOfTheTransitProcedure/name AND
            /*/ HolderOfTheTransitProcedure/Address/streetAndNumber AND
            /*/Consignment/Consignor/name AND
            /*/Consignment/Consignor/Address/streetAndNumber AND
            /*/Consignment/Consignee/name AND
            /*/Consignment/Consignee/Address/streetAndNumber AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/name AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/streetAndNumber AND
            /*/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/referenceNumber AND
            /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/referenceNumber AND
            /*/Consignment/ActiveBorderTransportmeans/conveyanceReferenceNumber AND
            /*/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/referenceNumber AND
            /*/Consignment/LocationOfGoods/Address/streetAndNumber AND
            /*/Consignment/GuaranteeReference/Guarantor/Address/streetAndNumber AND
            /*/Consignment/GuaranteeReference/Guarantor/name AND
            /*/ Consignment/TransportDocument/referenceNumber

            format shall be set to an..35
  </td>
</tr>


</table>
## RULE E1105

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks

            format shall be set to an..42
  </td>
</tr>


</table>
## RULE E1107

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/descriptionOfGoods

            format shall be set to an..280
  </td>
</tr>


</table>
## RULE E1109

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Consignment/grossMass AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass AND
            /*/Consignment/HouseConsignment/ConsignmentItem/ Commodity/GoodsMeasure/netMass
            format shall be set to n..11,3
  </td>
</tr>


</table>
## RULE E1111

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages

            format of shall be set to n..5
  </td>
</tr>


</table>
## RULE E1114

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Consignment/PlaceOfLoading/location

            format shall be set to an..17
  </td>
</tr>


</table>
## RULE E1117

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/complementOfInformation
            /*/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/complementOfInformation

            format shall be set to an..26.
  </td>
</tr>


</table>
## RULE E1118

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Guarantee/GuaranteeReference/accessCode

            format shall be set to an4
  </td>
</tr>


</table>
## RULE E1301

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Consignment/PreviousDocument AND
            /*/Consignment/SupportingDocument AND
            /*/Consignment/AdditionalReference AND
            /*/Consignment/AdditionalInformation AND
            /*/Consignment/HouseConsignment/countryOfDispatch AND
            /*/Consignment/HouseConsignment/referenceNumberUCR
            /*/Consignment/HouseConsignment/Consignor AND
            /*/Consignment/HouseConsignment/Consignee AND
            /*/Consignment/HouseConsignment/DepartureTransportMeans AND
            /*/Consignment/ HouseConsignment/PreviousDocument AND
            /*/Consignment/HouseConsignment/TransportDocument AND
            /*/Consignment/HouseConsignment/AdditionalReference

            shall not be used
  </td>
</tr>


</table>
## RULE E1401

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument
            multiplicity shall be set to '9x'
  </td>
</tr>


</table>
## RULE E1402

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN /*/Consignment/HouseConsignment/ConsignmentItem
            /*/FunctionalError
            /*/RiskAnalysisIdentification/RiskAnalysis

            multiplicity shall be set to '999x'
  </td>
</tr>


</table>
## RULE E1406

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN
            /*/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult AND
            /*/Consignment/ActiveBorderTransportMeans AND
            /*/Consignment/HouseConsignment AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/DangerousGoods
            multiplicity shall be set to '1x'
  </td>
</tr>


</table>
## RULE G0002

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   XSD contains a non-standard regular expression for this data item.
  </td>
</tr>


</table>
## RULE G0006

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   &lt;TRANSPORT EQUIPMENT-GOODS REFERENCE.Declaration goods item number&gt; is filled in with the item number of the goods concerned as provided in Declaration goods item number.
  </td>
</tr>


</table>
## RULE G0014

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Eastern longitude and Northern latitude will use the optional '+' sign.
            Western longitude and Southern latitude will use the '-' sign.
  </td>
</tr>


</table>
## RULE G0017

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   'State of seals' = 1 in case that Seals are in good state (i.e. present and not damaged)
            'State of seals' = 0 in case that Seals are not in good state (i.e. not present or damaged).
  </td>
</tr>


</table>
## RULE G0020

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Refers to the mode of transport corresponding to the active means of transport which is expected to be used on exit from or entry into the Safety and Security area.
  </td>
</tr>


</table>
## RULE G0023

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The D.I. will be filled in with new value amending initial declaration in case of incident
  </td>
</tr>


</table>
## RULE G0024

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   D.I. will be filled if the value is provided.
  </td>
</tr>


</table>
## RULE G0026

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This D.G. can be used only
            - in case of Export followed by transit (maximum one MRN included per one House Consignment)
            AND
            - if the &lt;TRANSIT OPERATION.Additional Declaration Type&gt; is EQUAL to 'A'.
  </td>
</tr>


</table>
## RULE G0029

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The D.I. will be filled in with new value amending initial declaration in case of incident. In case the initial container is replaced by another container then &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is equal to '1' else &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is equal to '0'.
  </td>
</tr>


</table>
## RULE G0030

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF Declaration type is in SET {T2, T2F}
            THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R" (optional for Destination San Marino)
            ELSE IF &lt;CUSTOMS OFFICE OF DEPARTURE (DECLARED)&gt; AND &lt;CUSTOMS OFFICE OF DESTINATION (DECLARED)&gt; are located in the same country
            THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "O"
            ELSE IF &lt;CUSTOMS OFFICE OF DEPARTURE (DECLARED)&gt; OR &lt;CUSTOMS OFFICE OF DESTINATION (DECLARED)&gt; is in a CTC country or
            Andorra
            THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R"
            ELSE &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "O"
  </td>
</tr>


</table>
## RULE G0033

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The Data Item &lt;AUTHORISATION.Reference number&gt; must be valid in CDMS or in the National Decision Management System.
  </td>
</tr>


</table>
## RULE G0042

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This D.G./D.I. is not used to report discrepancies. The Control Message always reports back D.G./D.I as at declaration message.
  </td>
</tr>


</table>
## RULE G0045

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The information in this Data Group/Data Item will override the information included in the CC015C (or in the latest CC013C, if any).
  </td>
</tr>


</table>
## RULE G0057

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Common Code List can be extended or restricted at national level. Purely national codes are not included in Common Domain messages.
  </td>
</tr>


</table>
## RULE G0058

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   D.I. is required in case of 'Export Followed By Transit' of excise goods.
  </td>
</tr>


</table>
## RULE G0061

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The information presented in in this D.G. is related to Safety &amp; Security and to the Binding Itinerary. In case of Binding itinerary, the information entered must include the list of codes of the countries between the Office of Departure and the Office of Destination. If more information is available about the countries visited by the means of transport since it's first place of loading until the last place of unloading, it should also be added for Safety &amp; Security purpose only.
  </td>
</tr>


</table>
## RULE G0088

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   When &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3', the identification number of the trailer must also be provided (where applicable).
  </td>
</tr>


</table>
## RULE G0089

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   During the Transitional Period (TP), the native CC015C, CC013C and CC170C sent to the National Transit Application shall not include the value ‘99’. This value ‘99’ is valid in CL750 during TP, only in case the value ‘99’ is the result of the upgrade by the National Transit Application of a legacy message (e.g. CC015B upgraded into CC015C).
  </td>
</tr>


</table>
## RULE G0090

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The Data Group ‘Carrier’ shall be provided if the value is different from the “Holder of the transit procedure”.
  </td>
</tr>


</table>
## RULE G0091

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   During the Transitional Period (TP), the native CC015C, CC013C and CC170C sent to the National Transit Application shall not include the value ‘99’. This value ‘99’ is valid in CL750 during TP, only in case the value ‘99’ is the result of the upgrade by the National Transit Application of a legacy message (e.g. CC015B upgraded into CC015C).
  </td>
</tr>


</table>
## RULE G0101

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The value of the Data Item &lt;INVALIDATION.Initiated by customs&gt; is
            ‘0’ ('No') when the request to invalidate is initiated by the trader;
            The value of the Data Item &lt;INVALIDATION.Initiated by customs&gt; is
            ‘1’ ('Yes') when the request to invalidate is initiated by the customs.
  </td>
</tr>


</table>
## RULE G0102

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   For each type of authorisation, the authorisation is valid for the whole declaration (i.e. for the different HOUSE CONSIGNMENTS).
  </td>
</tr>


</table>
## RULE G0103

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Each iteration of this data group shall include:
            -Either the transport equipment information for the containerised goods with seals OR without seals with reference to those goods;
            -OR the transport equipment information for the non containerised but sealed goods (e.g. goods carried by truck with seals) with reference to those goods;
            Note: the non containerised and unsealed goods shall not be recorded under this data group.
  </td>
</tr>


</table>
## RULE G0105

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Information recorded under this data group is solely for communication purposes. No legal liabilities exist upon the specific contact person.
  </td>
</tr>


</table>
## RULE G0112

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   If IMO ship identification number (type ‘10’) exists for that ship, it must be used and the Name of the
            sea-going vessel (type ‘11’) shall not be used.
  </td>
</tr>


</table>
## RULE G0114

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Functional Description:
            The Data Item “/*/AUTHORISATION/type” shall include the value ‘C521’ when the transit declaration is
            submitted under simplified procedure (authorised consignor) and only in this case.
  </td>
</tr>


</table>
## RULE G0115

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This Data Item is required as per UCC-DA (Annex B) but may be waived for modes of transport other than rail in case the transit movement does not cross the external border of the Union.
  </td>
</tr>


</table>
## RULE G0116

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Functional Description:
            During the Transitional Period, the data item “Customs office at border reference number”, is required
            for ‘native CC015C’ and ‘native CC013C’ and optional if CC013C or CC015C is the outcome of the
            upgraded CC013B or CC015B respectively. After the end of the Transitional Period, the data item will
            be always required.
  </td>
</tr>


</table>
## RULE G0117

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Functional Description:
            Common Code List can be extended at national level. Purely national codes are not included in
            Common Domain messages.
  </td>
</tr>


</table>
## RULE G0118

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Functional Description:
            IF the declaration is lodged without Safety and Security data then:
            • where goods are carried in multimodal transport units, such as containers, swap bodies and semi
            trailers, the customs authorities may authorise the holder of the transit procedure not to provide this
            information where the logistical pattern at the point of departure may prevent the identity and
            nationality of the means of transport from being provided at the time the goods are released for transit,
            providing multimodal transport units bear unique numbers and such numbers are indicated in D.E. 19
            07 063 000 Container identification number
            • In the following cases, Member States shall waive the obligation to enter this information on a transit
            declaration lodged at the office of departure in relation with the means of transport on which the goods
            are directly loaded:
            o where the logistical pattern does not allow this data element to be provided and the holder of the
            transit procedure has the AEOC status and
            o where the relevant information may be traced where needed by the customs authorities via the
            records of the holder of the transit procedure.
  </td>
</tr>


</table>
## RULE G0119

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This Data Group is “Required” except where one of the following conditions apply:
            • For the declaration that include Inland Mode Of Transport with the value ‘5’;
            • Where goods are carried in multimodal transport units, such as containers, swap bodies and semi trailers, the customs authorities may authorise the holder of the transit procedure not to provide this information where the logistical pattern at the point of departure may prevent the identity and nationality of the means of transport from being provided at the time the goods are released for transit, providing multimodal transport units bear unique numbers and such numbers are indicated in the Data Item ‘Container identification number’;
            • For the means of transport on which the goods are directly loaded:
            o	the logistical pattern does not allow this data element to be provided and the holder of the transit procedure has the appropriate status (AEOC in EU) and
            o	the relevant information may be traced where needed by the customs authorities via the records of the holder of the transit procedure.
  </td>
</tr>


</table>
## RULE G0120

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The Data Item ‘Identification number’ is required for the Data Group ‘HOLDER OF THE TRANSIT PROCEDURE’, except for:
            - economic operators residing outside of the common transit countries (outside CL009), and
            - private individuals for which an identification number may be used but is not required.
  </td>
</tr>


</table>
## RULE G0123

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This Data Group must be provided when different from the ‘HOLDER OF THE TRANSIT PROCEDURE’.
            IF the unique ‘CONSIGNOR’ of the consignment is different from the ‘HOLDER OF THE TRANSIT PROCEDURE’
            THEN  the Data Group &lt;CONSIGNMENT - CONSIGNOR&gt; must include this ‘CONSIGNOR’;
            IF the ‘CONSIGNOR’ of one or more house consignment(s) is different from the ‘HOLDER OF THE TRANSIT PROCEDURE’
            THEN  the Data Group &lt;CONSIGNMENT – HOUSE CONSIGNMENT - CONSIGNOR&gt; must include this ‘CONSIGNOR’.
  </td>
</tr>


</table>
## RULE G0165

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the use of seals,
            THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'.
  </td>
</tr>


</table>
## RULE G0186

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   &lt;UNLOADING REMARK.Unloading completion&gt; is used as a flag and it can contain 2 possible values:
                 ‘0’ = ‘NO’ This means that the unloading of the goods is not yet completed;
                 ‘1’ = ‘YES’ This means that the goods are completely unloaded.
  </td>
</tr>


</table>
## RULE G0196

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This data group must contain the full transport equipment details and not only what is different compared to the data declared in the customs declaration.
  </td>
</tr>


</table>
## RULE G0200

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The value of the Data Item &lt;UNLOADING REMARK.State of seals&gt; is '1' ('Yes') when the Seals are in good state (i.e. present and not damaged);
            The value of the Data Item &lt;UNLOADING REMARK.State of seals&gt; is '0' ('No') when the Seals are not in good state (i.e. not present or damaged).
  </td>
</tr>


</table>
## RULE G0201

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Rule R0840 shall be validated only by MS. IF the sender is a CTC country THEN the &lt;CUSTOMS OFFICE OF TRANSIT&gt; in MS, that detects the violation of R0840, should request a new ENS declaration before it authorizes the goods to enter the EU. The message CD050C or CD115C from a CTC country may not be rejected if R0840 is violated.
  </td>
</tr>


</table>
## RULE G0205

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   &lt;UNLOADING REMARK.Conform&gt; is used as a flag and it can contain 2 possible values:
            ‘0’ = ‘NO’ there are unloading remarks;
            ‘1’ = ‘YES’ no unloading remarks present.
  </td>
</tr>


</table>
## RULE G0300

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The UN Number must be present if the commodity includes dangerous goods that are listed in the United Nations Dangerous Goods Code (UNDG).
  </td>
</tr>


</table>
## RULE G0301

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The Data Item &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY.CUS code&gt; can be used when the CL016 (CUSCode) in CS/RD2 includes [CUS code &amp; CN code] where the CN code matches with the &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY CODE. Harmonized System sub-heading code&gt; &amp; &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY CODE.Combined nomenclature code&gt;.
  </td>
</tr>


</table>
## RULE G0332

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Container indicator&gt; is NOT PRESENT then data group &lt;TRANSPORT EQUIPMENT&gt; shall NOT be PRESENT, too. &lt;Container indicator&gt; functions as the governing data item for data group &lt;TRANSPORT EQUIPMENT&gt;.
  </td>
</tr>


</table>
## RULE G0500

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Value 'T' must only be used in case “House number” and “Postcode” or only “Postcode” define an exact and unique location
  </td>
</tr>


</table>
## RULE G0670

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   If all goods items are related a single container, the data group can be omitted.
            Otherwise all the goods items related to this container (if present) must be declared.
            All the non-containerised goods items related to this seals information (if present) must be declared as well.
  </td>
</tr>


</table>
## RULE G0789

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The ’Customs office at border reference number’ identifies the border crossing point (BCP) where the ‘Active border transport means’ will be present. It is either the ‘Reference number’ of one of the ‘CUSTOMS OFFICE OF TRANSIT (DECLARED)’ or the ‘Reference number’ of one of the ‘CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)’ or the ‘Reference number’ of the ‘CUSTOMS OFFICE OF DESTINATION (DECLARED)’. By using this Data Item, it is possible (after the end of the Transitional Period) to identify which transport means will be present at which border crossing point, in case of multiple BCP and multiple changes of active transport means.
  </td>
</tr>


</table>
## RULE G0825

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   - Consignment related information shall be recorded under
            &lt;CONSIGNMENT-ADDITIONAL SUPPLY CHAIN ACTOR&gt;
            &lt;CONSIGNMENT-PREVIOUS DOCUMENT&gt;
            &lt;CONSIGNMENT-SUPPORTING DOCUMENT&gt;
            &lt;CONSIGNMENT-TRANSPORT DOCUMENT&gt;
            &lt;CONSIGNMENT-ADDITIONAL REFERENCE&gt;
            &lt;CONSIGNMENT-ADDITIONAL INFORMATION&gt;
            - House Consignment related information shall be recorded under+
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL SUPPLY CHAIN ACTOR&gt;
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT&gt;
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT DOCUMENT&gt;
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-ADDITIONAL REFERENCE&gt;
            - Goods item related information shall be recorded under
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL SUPPLY CHAIN ACTOR&gt;
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS DOCUMENT&gt;
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-SUPPORTING DOCUMENT&gt;
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL REFERENCE&gt;
            &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL INFORMATION&gt;
  </td>
</tr>


</table>
## RULE G0850

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This Data Group must be filled in if a &lt;REPRESENTATIVE&gt; is used by the &lt;HOLDER OF THE TRANSIT PROCEDURE&gt;.
  </td>
</tr>


</table>
## RULE G0988

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The Country of dispatch can be different from the Country defined in the address of the Consignor.
  </td>
</tr>


</table>
## RULE GN001

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   HOLDER OF THE PROCEDURE  specifies the price in EUR of the declared goods corresponding to the last sales price of goods sold internationally before release into transit mode.
            If not specified otherwise, the price is "0" if the goods are not sold or paid for.
  </td>
</tr>


</table>
## RULE GN002

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   MRN must comply with the structure of fallback MRN.
  </td>
</tr>


</table>
## RULE GRN

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   GRN musí splňovat kontrolní součet dle ISO 6346.
  </td>
</tr>
<tr>
<td class="Label">
   Description (CS)
  </td>
<td>
<pre>GRN musí splňovat kontrolní součet dle ISO 6346.</pre>
</td>
</tr>

<tr>
<td class="Label">
   Description (SR)
  </td>
<td>
<pre>GRN mora da zadovolji algoritam naveden u ISO 6346.</pre>
</td>
</tr>

</table>
## RULE R0007

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Each /*/Consignment/HouseConsignment/ConsignmentItem/declarationGoodsItemNumber is unique throughout the declaration. The items shall be numbered in a sequential fashion, starting from '1' for the first item and increment the numbering by '1' for each following item.
  </td>
</tr>


</table>
## RULE R0020

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Transit Operation/declarationType is EQUAL to 'T2'
            AND the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in SET CL112
            THEN the /*/HolderOfTheTransitProcedure must declare at least one
            (/*/Consignment/PreviousDocument OR
            /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument)
            with Data Item ‘type’ in SET CL178.
  </td>
</tr>


</table>
## RULE R0021

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   A zero '0' is to be considered as a valid number in this field.
  </td>
</tr>


</table>
## RULE R0028

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The structure of this Data Item is validated as specified in DDCOM. The check digit must follow the ISO 6346 standard.
  </td>
</tr>


</table>
## RULE R0060

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/
            CommodityCode/combinedNomenclatureCode is PRESENT
            THEN the concatenation of the Data Items /*/Consignment/HouseConsignment/
            ConsignmentItem/Commodity/CommodityCode/harmonizedSystemSubHeadingCode (an6) and /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/
            CommodityCode/combinedNomenclatureCode (an2) must be a valid code in the TARIC database (validated only by the EU countries).
  </td>
</tr>


</table>
## RULE R0076

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/ActiveBorderTransportMeans/typeOfIdentification is in SET {10,21,30,40,41,80}
            THEN /*/Consignment/ActiveBorderTransportMeans/identificationNumber shall not contain lowercase
            letters.
  </td>
</tr>


</table>
## RULE R0100

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The D.G./D.I. is used as the basic language to be used in any further communication between the Trader and the Customs system. If is PRESENT, the indicated language is used as the basic language in any further communication between the Trader and the Customs system. If not PRESENT then the Customs system will use the default language of the Office concerned.
  </td>
</tr>


</table>
## RULE R0102

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Data item /*/Invalidation.decision can contain 2 valid values:
            - ‘0’ = ‘No’: Invalidation refused by Customs: Decision
            - ‘1’ = ‘Yes’: Invalidation accepted by Customs: Decision
  </td>
</tr>


</table>
## RULE R0103

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   /*/CustomsOfficeOfExitForTransitDeclared/referenceNumber is NOT EQUAL to
            /*/CustomsOfficeOfDestinationDeclared/referenceNumber
            AND
            IF /*/CustomsOfficeOfTransitDeclared is PRESENT
            THEN
            /*/CustomsOfficeOfExitForTransitDeclared/referenceNumber is NOT EQUAL to
            /*/CustomsOfficeOfTransiDeclared/referenceNumber
  </td>
</tr>


</table>
## RULE R0106

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   /*/TransportEquipment/numberOfSeals is EQUAL to the ‘maximum value of /*/TransportEquipment/Seal/sequenceNumber’.
  </td>
</tr>


</table>
## RULE R0107

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   &lt;TRANSPORT EQUIPMENT-SEAL.Identifier&gt; is unique in the whole declaration.
  </td>
</tr>


</table>
## RULE R0165

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the use of seals
            THEN /*/Consigngment/TransportEquipment/numberOfSeals&gt; is GREATER than '0'.
  </td>
</tr>


</table>
## RULE R0221

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to ‘0’
            THEN
            for this CONSIGNMENT ITEM
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass is EQUAL to ‘0’
            AND
            for this HOUSE CONSIGNMENT at least one CONSIGNMENT ITEM must exist with
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass having a value different from ‘0’
            ELSE for this CONSIGNMENT ITEM
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass must be different from ‘0’.
  </td>
</tr>


</table>
## RULE R0223

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass is GREATER THAN ‘0’ (zero)
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass must be LESS THAN OR EQUAL to /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass.
  </td>
</tr>


</table>
## RULE R0315

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Where /*/Consignment/mode OfTransportAtTheBorder is EQUAL to '4' the (IATA/ICAO) flight number shall be indicated and shall have a format an..8:
            - an..3: mandatory prefix identifying the airline/operator
            - n..4: mandatory number of the flight
            - a1: optional suffix
  </td>
</tr>


</table>
## RULE R0318

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Guarantee/guaranteeType is EQUAL to '4'
            THEN the format of /*/Guarantee/GuaranteeReference/GRN is 'an24'
            ELSE the format of /*/Guarantee/GuaranteeReference/GRN is 'an17'
  </td>
</tr>


</table>
## RULE R0350

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/reducedDatasetIndicator&gt; is EQUAL to '1'
            AND /*/Consignment/inlandModeOfTransport is in SET {1, 2, 4}
            THEN
            at least one /*/Authorisation/type is EQUAL to 'C524'
  </td>
</tr>


</table>
## RULE R0352

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/reducedDatasetIndicator&gt; is EQUAL to '1'
            AND /*/Consignment/inlandModeOfTransport is in SET {1, 2, 4}
            THEN
            this Data Item includes at least one &lt;Authorisation number&gt; for a valid Authorisation for Reduced Data Set owned by the Holder of the Transit Procedure
  </td>
</tr>


</table>
## RULE R0364

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to ‘0’
            THEN for this HOUSE CONSIGNMENT at least one CONSIGNMENT ITEM must exist with
            (the same /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages AND
            the same /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/shipingMarks AND
            with /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages having a value GREATER than ‘0’).
  </td>
</tr>


</table>
## RULE R0410

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC015C/TransitOperation/security (the transit declaration includes ENS data for safety and security purposes [only]) is EQUAL to ‘1’
            THEN the 17th character of MRN is EQUAL to 'L'
            ELSE IF /*/TransitOperation/security (the transit declaration includes EXS data for safety and security purposes [only]) is EQUAL to EQUAL to ‘2’
            THEN the 17th character of MRN is EQUAL to 'K'
            ELSE IF */TransitOperation/security (the transit declaration includes ENS and EXS data for safety and security purposes [only]) is EQUAL to ‘3’
            THEN the 17th character of MRN is EQUAL to 'M'
            ELSE the 17th character of MRN is EQUAL to 'J'
  </td>
</tr>


</table>
## RULE R0416

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The Data Item /*/Consignment/HouseConsignment/PreviousDocument/referenceNumber must include a valid export MRN. The 17th character must be in SET {A, B}.
  </td>
</tr>


</table>
## RULE R0448

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/TransportEquipment/containerIdentificationNumber is NOT PRESENT
            THEN the R0021 is not applicable (i.e. the value '0' is not valid) for
            /*/Consignment/TransportEquipment/numberOfSeals;

            IF /*/Consignment/Incident/TransportEquipment/containerIdentificationNumber is NOT PRESENT
            THEN the R0021 is not applicable (i.e. the value '0' is not valid) for
            /*/Consignment/Incident/TransportEquipment/numberOfSeals
  </td>
</tr>


</table>
## RULE R0472

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/inlandModeOfTransport is in SET {1,2,3,4,8}
            THEN
            IF /*/Consignment/DepartureTransportMeans is PRESENT
            THEN the first digit of /*/Consignment/DepartureTransportMeans/typeOfIdentification shall be EQUAL to /*/Consignment/inlandModeOfTransport
            ELSE
            IF /*/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT
            THEN the first digit of /*/Consignment/HouseConsignment/ DepartureTransportMeans/typeOfIdentification shall be EQUAL to /*/Consignment/inlandModeOfTransport
  </td>
</tr>


</table>
## RULE R0473

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/DepartureTransportMeans is PRESENT AND /*/Consignment/DepartureTransportMeans/typeofIdentification is in SET {10,20,21,30,31,40,41,80}
            THEN /*/Consignment/DepartureTransportMeans/IdentificationNumber shall not contain lowercase letters
            ELSE
            IF /*/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT AND /*/Consignment/HouseConsignment/DepartureTransportMeans/typeofIdentification is in SET {10,20,21,30,31,40,41,80}
            THEN /*/Consignment/HouseConsignment/DepartureTransportMeans/IdentificationNumber shall not contain lowercase letters
  </td>
</tr>


</table>
## RULE R0474

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/inlandModeOfTransport is EQUAL to '3'
            THEN the first data group iteration /*/Consignment/DepartureTransportMeans/typeOfIdentification must be EQUAL to '30';
            IF /*/Consignment/inlandModeOfTransport is EQUAL to '3'
            AND /*/Consignment/House Consignment/DepartureTransportMeans is PRESENT
            THEN for this House Consignment, the first data group iteration   /*/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification must be EQUAL to '30'.
  </td>
</tr>


</table>
## RULE R0476

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/inlandModeOfTransport is EQUAL to '3'
            THEN
            IF the multiplicity of the data group /*/Consignment/DepartureTransportMeans is more than 1x
            THEN the iteration 2 and the iteration 3 (if present) of the data group /*/Consignment/DepartureTransportMeans must include /*/Consignment/DepartureTransportMeans/typeOfIdentification that is EQUAL to '31'
            ELSE
            IF the multiplicity of the data group /*/Consignment/HouseConsignment/DepartureTransportMeans is more than 1x
            THEN the iteration 2 and the iteration 3 (if present) of the data group /*/Consignment/HouseConsignment/DepartureTransportMeans must include /*/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification that is EQUAL to '31'
  </td>
</tr>


</table>
## RULE R0506

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/Consignor is PRESENT for all /*/Consignment/HouseConsignment/
            THEN at least one occurrence of /*/Consignment/HouseConsignment/Consignor must be different from the others;

            IF /*/Consignment/HouseConsignment/Consignee is PRESENT for all /*/Consignment/HouseConsignment/
            THEN at least one occurrence of /*/Consignment/HouseConsignment/Consignee must be different from the others;

            IF /*/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT for all /*/Consignment/HouseConsignment
            THEN at least one occurrence of /*/Consignment/HouseConsignment/DepartureTransportMeans must be different from the others;

            IF /*/Consignment/HouseConsignment/referenceNumberUCR is PRESENT for all /*/Consignment/HouseConsignment/
            THEN at least one occurrence of /*/Consignment/HouseConsignment/referenceNumberUCR must be different from the others;

            IF /*/Consignment/HouseConsignment/countryOfDispatch is PRESENT for all /*/Consignment/HouseConsignment/
            THEN at least one occurrence of /*/Consignment/HouseConsignment/countryOfDispatch must be different from the others.
  </td>
</tr>


</table>
## RULE R0507

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/Consignee is PRESENT for all /*/Consignment/HouseConsignment/ConsignmentItem
            THEN at least one occurrence of /*/Consignment/HouseConsignment/ConsignmentItem/Consignee must be different from the others;

            IF /*/Consignment/HouseConsignment/ConsignmentItem/TransportCharges is PRESENT for all /*/Consignment/HouseConsignment/ConsignmentItem
            THEN at least one occurrence of /*/Consignment/HouseConsignment/ConsignmentItem/TransportCharges must be different from the others;

            IF /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is PRESENT for all /*/Consignment/HouseConsignment/ConsignmentItem
            THEN at least one occurrence of /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination must be different from the others;

            IF /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR is PRESENT for all /*/Consignment/HouseConsignment/ConsignmentItem
            THEN at least one occurrence of /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR must be different from the others;

            IF /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch is PRESENT for all /*/Consignment/HouseConsignment/ConsignmentItem
            THEN at least one occurrence of /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch must be different from the others.
  </td>
</tr>


</table>
## RULE R0601

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/type&gt; is EQUAL to 'C651'
            THEN (
            IF /*/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT
            THEN ( /*/Consignment/HouseConsignment/ConsignmentItem/declarationType is EQUAL to ‘T1’ AND
            /*/TransitOperation/declarationType is EQUAL to ‘T’ ) )
            ELSE /*/TransitOperation/declarationType is EQUAL to ‘T1’
  </td>
</tr>


</table>
## RULE R0789

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF/*/CustomsOfficeOfTransitDeclared is PRESENT
            THEN the multiplicity of /*/Consignment/ActiveBorderTransportMeans is up to 9x
            ELSE the multiplicity of /*/Consignment/ActiveBorderTransportMeans is 1x
  </td>
</tr>


</table>
## RULE R0817

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   When /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/type is EQUAL to 'C651' the Unique Body Reference (UBR) shall be recorded in this field.
  </td>
</tr>


</table>
## RULE R0840

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Only a valid EORI or TCUIN shall be used. The EORI shall be validated only by EU MS. The TCUIN shall be validated by EU MS and by the country where the TCUIN is defined.

            The EORI/TCUIN values should comply with the following pattern: &lt;xs:pattern value="[A-Z]{2}[\x21-\x7E]{1,15}"/&gt;.
  </td>
</tr>


</table>
## RULE R0849

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType IS EQUAL TO ‘TIR’  (and to 'TIRME')
            THEN /*/TransitOperation/reducedDatasetIndicator = “0”;
            IF /*/Authorisation/type is EQUAL TO ‘C524’
            THEN /*/TransitOperation/reducedDatasetIndicator = “1”
  </td>
</tr>


</table>
## RULE R0850

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF sender is in EU (CL010)
            THEN the value must be a valid EORI or TCUIN (validated by receiver, if located in EU),
            ELSE (sender is not in EU) the value must be a TIN number (validated by the message sender only).
            The EORI/TCUIN values should comply with the following pattern: &lt;xs:pattern value=" [A-Z]{2}[\x21-\x7E]{1,15}"/&gt;
  </td>
</tr>


</table>
## RULE R0851

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The Identification number can be validated if the Consignee is located in the same contracting party as the Recipient.
  </td>
</tr>


</table>
## RULE R0855

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/inlandModeOfTransport is EQUAL to ‘3’
            THEN the multiplicity of /*/Consignment/DepartureTransportMeans AND /*/Consignment/HouseConsignment/DepartureTransportMeans can be up to '3x'
            ELSE
            IF /*/Consignment/inlandModeOfTransport is EQUAL to ‘2’
            THEN the multiplicity of /*/Consignment/DepartureTransportMeans AND /*/Consignment/HouseConsignment/DepartureTransportMeans can be more than '1x'
            ELSE the multiplicity of /*/Consignment/DepartureTransportMeans AND /*/Consignment/HouseConsignment/DepartureTransportMeans is '1x'
  </td>
</tr>


</table>
## RULE R0900

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to 'TIR'  (and to 'TIRME')
            THEN /*/Guarantee/guaranteeType is EQUAL to 'B'
            ELSE
            IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in SET CL010 OR is EQUAL to 'SM' OR is EQUAL to 'AD'
            THEN /*/Guarantee/guaranteeType must be in SET CL230
            ELSE /*/Guarantee/guaranteeType must be in SET CL229
  </td>
</tr>


</table>
## RULE R0901

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to 'TIR'
            THEN the first two characters of /*/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET CL010
            AND the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in SET CL010
  </td>
</tr>


</table>
## RULE R0904

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in SET {AD, SM}
            THEN the first two characters of /*/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET CL553
  </td>
</tr>


</table>
## RULE R0905

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in SET CL112
            THEN the two characters of /*/CustomsOfficeOfDestinationDeclared/referenceNumber is NOT in SET{AD, SM}
  </td>
</tr>


</table>
## RULE R0906

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the first two characters of /*/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to ‘AD’
            THEN the first two characters of /*/CustomsOfficeOfDTransitDeclared/referenceNumber is EQUAL to ‘AD’;
            IF the first two characters of /*/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to ‘AD’
            THEN the first two characters of /*/CustomsOfficeOfDTransitActual/referenceNumber is EQUAL to ‘AD’
  </td>
</tr>


</table>
## RULE R0909

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the first two characters of /*/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to 'SM'
            THEN
            IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'IT',
            THEN /*/TransitOperation/declarationType is EQUAL to 'T2SM' AND
            /*/Consignment/HouseConsignment/ConsignmentItem/declarationType = "N"
            ELSE
            IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in set CL010 AND
            NOT EQUAL to 'IT'
            THEN /*/TransitOperation/declarationType is in SET {T2, T2F} OR /*/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2, T2F};

            IF the first two characters of /*/CustomsOfficeOfDestinationActual/referenceNumber is EQUAL to 'SM'
            THEN
            IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'IT',
            THEN /*/TransitOperation/declarationType is EQUAL to 'T2SM' AND /*/Consignment/HouseConsignment/ConsignmentItem/declarationType = "N"
            ELSE
            IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in set CL010 AND NOT EQUAL to "IT'
            THEN /*/TransitOperation/declarationType is in SET {T2, T2F} OR /*/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2, T2F}
  </td>
</tr>


</table>
## RULE R0911

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'SM' AND
            the first two characters of /*/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET CL010
            THEN
            /*/TransitOperation/declarationType is in SET {T2, T2F} AND
            /*/Consignment/HouseConsignment/ConsignmentItem/declarationType = "N";

            IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'SM' AND
            the first two characters of /*/CustomsOfficeOfDestinationActual/referenceNumber is in SET CL010
            THEN
            /*/TransitOperation/declarationType is in SET {T2, T2F} AND
            /*/Consignment/HouseConsignment/ConsignmentItem/declarationType = "N"
  </td>
</tr>


</table>
## RULE R0983

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   /*/Consignment/HouseConsignment/grossMass must be GREATER than OR EQUAL to the sum of /*/Consignment/HouseConsignmentConsignmentItem/Commodity/GoodsMeasure/grossMass available for all Consignment Items included in that House Consignment
  </td>
</tr>


</table>
## RULE R0987

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Each &lt;Sequence number&gt; is unique for the Data Group it belongs to. The sequence numbers shall be sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each iteration.
  </td>
</tr>


</table>
## RULE R0988

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Each &lt; Goods item number&gt; is unique for the Data Group it belongs to. The Goods item number shall be sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each iteration.
  </td>
</tr>


</table>
## RULE R0990

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The /*/TransitOperation/TIRCarnetNumber must have the format an10 or an11 and must follow the algorithm defined by IRU, see DDNTA Main Document.
  </td>
</tr>


</table>
## RULE R0994

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The value of /*/Consignment/grossMass must be GREATER than or EQUAL to the sum of /*/Consignment/HouseConsignment/grossMass for all house consignments.
  </td>
</tr>


</table>
## RULE R3060

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/countryOfDestination is in SET CL009
            OR
            at least one /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET CL009
            THEN /*/Consignment/AdditionalInformation/code shall not be EQUAL TO '30600'
  </td>
</tr>


</table>
## RULE R3061

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/countryOfDestination is in SET CL009
            OR
            /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination of THIS Consignment Item is in SET CL009
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/AdditionalInformation/code of this Consignment Item shall not be EQUAL TO '30600'
  </td>
</tr>


</table>
## RULE RN001

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is NOT in SET {T1ME, TIRME, ATA, SCDIM, SCDEX} and
            the country code  (first two digits) Customs office of Destination is Montenegro,
            at least TWO Customs offices of Transit must be used and the country code (first two digits) of last Customs office of Transit must be Montenegro
  </td>
</tr>


</table>
## RULE RN002

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is in SET  {T1ME, T2ME,TIRME,ATA, SCDIM, SCDEX}
            THEN /*/TransitOperation/reducedDatasetIndicator = “0”
  </td>
</tr>


</table>
## RULE RN004

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The value of „TRANSIT OPERATION/Total value of goods“ must be  EQUAL
            to the sum of /*/Consignment/House consignemt/Consignemt Item/itemPriceEUR for all Goods Items
  </td>
</tr>


</table>
## RULE RN005

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Only EUR is valid vaule
  </td>
</tr>


</table>
## RULE RN008

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Combination of D.I. UnloadingRemark/Conform is true and UnloadingRemark/Conform is false is impossible
  </td>
</tr>

</table>
## RULE RN104

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Only Montenegrin customs office is acceptable with this item
  </td>
</tr>


</table>
## RULE RN117

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF simplified procedure is used (AUTHORISATION/Type = C521) THEN only guarantee type 0, 1 can be used.
  </td>
</tr>


</table>
## RULE RN134

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Combination of guarantee type and regime of transit operation must be allowed in the code list GuaranteeType_Transit.
  </td>
</tr>


</table>
## RULE RN154

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF both customs office of departure and customs office of destination are from European Union country
            OR Declaration Type is national transit ("'T1ME, T2ME,ATA, SCDIM, SCDEX ")
            THEN Guarantee type "5" can be used ELSE Guarantee type "5" cannot be used
  </td>
</tr>


</table>
## RULE RN159

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF country of Customs office of destination is not member of European Community and not AD or SM
            and Declaration type is not a national transit (T1ME, T2ME, TIRME, ATA, SCDIM, SCDEX )
            THEN at least one data group "Customs office of transit (box 51)" should contains customs office from the same country as country of Customs office of destination.
  </td>
</tr>


</table>
## RULE RN160

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF Guarantee type &lt;&gt; "4" THEN only one data group "Guarantee reference" can be used.
  </td>
</tr>


</table>
## RULE RN161

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   One guarantee cannot be used more than once in on transit declaration.
  </td>
</tr>


</table>
## RULE RN175

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   Authorisation for communication with Customs office of departure, which was filled into Envelope,
            must correspond with Holder of the procedure/Representative (in case of direct representation)
            and Customs office of departure.
  </td>
</tr>


</table>
## RULE RN177

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF Representatve is filled THEN must be different from Holder of the procedure
  </td>
</tr>


</table>
## RULE RN180

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   This element cannot be greater than current date.
  </td>
</tr>


</table>
## RULE RN181

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   "Fallback procedure indicator" can be set to "1" only when Simplified procedure at departure = "1".
  </td>
</tr>


</table>
## RULE RN190

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   For SAD initiated in Montenegro  „Declaration type 'T2SM' cannot be used.
  </td>
</tr>


</table>
## RULE RN202

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   For national transit declaration type (T1ME, T2ME,TIRME,ATA, SCDIM, SCDEX)
            only Montenegrin  customs office is acceptable with this item.
  </td>
</tr>


</table>
## RULE RN221

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF Declaration type="ATA" THEN Guarantee type shall be equal "D" ELSE Guarantee type shall not be equal "D".
  </td>
</tr>


</table>
## RULE RN223

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF "Declaration Type" = 'ATA' THEN "CONSIGNMENT-TRANSPORT DOCUMENT.Type"
            or "CONSIGNMENT- HOUSE CONSIGNMENT-TRANSPORT DOCUMENT.Type
            one occurrence must be EQUAL to „N955“.
  </td>
</tr>


</table>
## RULE RN239

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   If in envelope of message is specified the element MRN, then the value of this element must be the same like value in the element MRN in group Header of message.
  </td>
</tr>


</table>
## RULE RN242

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF ""CONSIGNMENT-TRANSPORT DOCUMENT.Type" or "CONSIGNMENT- HOUSE CONSIGNMENT-TRANSPORT DOCUMENT.Type“  is EQUAL to  N955' ,
            THEN „Reference number“  must be equal to element GUARANTEE.Other gurarantee reference  (if is used).
  </td>
</tr>


</table>
## RULE RN520

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the message CC013C is used for amending the Guarantee previously declared (i.e. the Data Item /*/TransitOperation/amendmentTypeFlag is EQUAL to ‘1')
            THEN
            the only difference between this CC013C and the CC015C (or the previous CC013C) shall can be located in the Data Group /*/Guarantee
            ELSE (the Data Item /*/TransitOperation/amendmentTypeFlag is EQUAL to ‘0')
            all Data Groups and Data Items of the original declaration can be amended, except the following Data Groups:
            - /*/HolderOfTheTransitProcedure (except of group */ContactPerson, which is possible to change)
            - /*/Representative (except of group */ContactPerson, which is possible to change)
            - /*/CustomsOfficeOfDeparture
            and the following Data Items:
            - /*/TransitOperation/additionalDeclarationType
            - /*/TransitOperation/declarationType
            - /*/TransitOperation/MRN
            - /*/TransitOperation/LRN
            - /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/harmonizedSystemSubHeadingCode
            - /*/TransitOperation/security
  </td>
</tr>

</table>
## RULE S1018

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The validation of particular Data Group/Item shall be performed in the following sequence: C0215 &gt; C0315
  </td>
</tr>


</table>
## RULE S1020

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   The validation of particular Data Group/Item shall be performed in the following sequence: C0030 &gt; C0105
  </td>
</tr>


</table>

# List of conditions
## CONDITION B1890

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;
            THEN R0855 will be disabled
            AND
            IF /*/Consignment/inlandModeOfTransport is EQUAL to ‘3’
            THEN the multiplicity of /*/Consignment/DepartureTransportMeans can be up to '3x'
            ELSE the multiplicity of /*/Consignment/DepartureTransportMeans is '1x'
  </td>
</tr>


</table>
## CONDITION C0001

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/countryOfDestination is in SET CL009
            THEN
            IF /*/Consignment/Consignee is PRESENT
            THEN
            /*/Consignment/HouseConsignment/Consignee = "N" AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE
            IF /*/Consignment/HouseConsignment/Consignee is PRESENT
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "R"
            ELSE
            IF /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET CL009
            THEN
            THIS /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "R"
            ELSE
            IF /*/TransitOperation/security is IN SET {0,1}
            THEN
            IF /*/Consignment/Consignee is PRESENT
            THEN
            /*/Consignment/HouseConsignment/Consignee = "N" AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE
            IF /*/Consignment/HouseConsignment/Consignee is PRESENT
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "O"
            ELSE
            IF /*/Consignment/AdditionalInformation/code is EQUAL TO '30600'
            THEN
            /*/Consignment/Consignee = "N" AND
            /*/Consignment/HouseConsignment/Consignee = "N" AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE
            IF /*/Consignment/HouseConsignment/ConsignmentItem/AdditionalInformation/code IS EQUAL TO '30600'
            THEN
            THIS /*/Consignment/HouseConsignment/Consignee = "N" AND
            THIS /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE
            IF /*/Consignment/Consignee is PRESENT
            THEN
            /*/Consignment/HouseConsignment/Consignee = "N" AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE
            IF /*/Consignment/HouseConsignment/Consignee is PRESENT
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"
            ELSE
            /*/Consignment/HouseConsignment/ConsignmentItem/Consignee = "R"
  </td>
</tr>


</table>
## CONDITION C0030

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to 'TIR'
            THEN /*/CustomsOfficeOfTransitDeclared = "N"
            ELSE /*/CustomsOfficeOfTransitDeclared = "O"
  </td>
</tr>


</table>
## CONDITION C0045

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to 'T'
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/declarationType = "R"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/declarationType = "N"
  </td>
</tr>


</table>
## CONDITION C0055

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/containerIndicator is EQUAL to '0'
            THEN /*/Consignment/TransportEquipment/containerIdentificationNumber = "N"
            ELSE at least one iteration of /*/Consignment/TransportEquipment/containerIdentificationNumber = "R" (for the rest of iterations is optional)
  </td>
</tr>


</table>
## CONDITION C0060

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages is in SET CL181
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks = "O"
            AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages = "N"
            ELSE IF /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages is in SET CL182
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks = "O"
            AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages = "R"
            ELSE
            /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks ="R"
            AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages = "R"
  </td>
</tr>


</table>
## CONDITION C0085

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Guarantee/guaranteeType is in SET CL076
            THEN /*/Guarantee/GuaranteeReference = "R"
            ELSE /*/Guarantee/GuaranteeReference = "N"
  </td>
</tr>


</table>
## CONDITION C0086

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Guarantee/guaranteeType is in SET CL286
            THEN /*/Guarantee/GuaranteeReference/GRN = "R" AND /*/Guarantee/GuaranteeReference/accessCode = "R"
            ELSE /*/Guarantee/GuaranteeReference/GRN = "N" AND /*/Guarantee/GuaranteeReference/accessCode = "N"
  </td>
</tr>


</table>
## CONDITION C0101

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/reducedDatasetIndicator is EQUAL to '1'
            THEN /*/Authorisation = "R"
            ELSE /*/Authorisation = "O"
  </td>
</tr>


</table>
## CONDITION C0102

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/simplifiedProcedure is EQUAL to '1'
            THEN /CC007C/Authorisation = "R"
            ELSE /CC007C/Authorisation = "N"
  </td>
</tr>


</table>
## CONDITION C0105

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/CustomsOfficeOfExitForTransitDeclared is PRESENT
            THEN /*/CustomsOfficeOfTransitDeclared = "R"
            ELSE /*/CustomsOfficeOfTransitDeclared = "O"
  </td>
</tr>


</table>
## CONDITION C0128

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Invalidation/initiatedByCustoms is EQUAL to ‘1’
            THEN /*/Invalidation/decision = "N"
            ELSE /*/Invalidation/decision = "R"
  </td>
</tr>


</table>
## CONDITION C0129

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Invalidation/initiatedByCustoms is EQUAL to ‘1’
            THEN /*/Invalidation/requestDateAndTime = "N"
            ELSE /*/Invalidation/requestDateAndTime = "R"
  </td>
</tr>


</table>
## CONDITION C0130

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Guarantee/guaranteeType is EQUAL to '8'
            THEN /*/Guarantee/otherGuaranteeReference = "R"
            ELSE IF /*/Guarantee/guaranteeType is EQUAL to '3'
            THEN /*/Guarantee/otherGuaranteeReference = "O"
            ELSE /*/Guarantee/otherGuaranteeReference = "N"
  </td>
</tr>


</table>
## CONDITION C0137

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF (/*/Invalidation/initiatedByCustoms is EQUAL to '0’ AND /*/Invalidation/decision is EQUAL to ‘0’) OR /*/Invalidation/initiatedByCustoms is EQUAL to ‘1’
            THEN /*/Invalidation/justification = "R"
            ELSE /*/Invalidation/justification = "O"
  </td>
</tr>


</table>
## CONDITION C0153

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/TIRCarnetNumber is PRESENT
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode = "O"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode = "R"
  </td>
</tr>


</table>
## CONDITION C0186

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/security is EQUAL to '0'
            THEN /*/Consignment/HouseConsignment/TransportCharges = "N"
            AND /*/Consignment/HouseConsignment/ConsignmentItem/TransportCharges = "N"
            ELSE /*/Consignment/HouseConsignment/TransportCharges = "O"
            AND /*/Consignment/HouseConsignment/ConsignmentItem/TransportCharges = "O"
  </td>
</tr>


</table>
## CONDITION C0191

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/security is in SET {1, 3}
            THEN
            /*/Consignment/PlaceOfUnloading = "R"
            ELSE
            IF /*/TransitOperation/security is EQUAL to ‘0’
            THEN
            /*/Consignment/PlaceOfUnloading = "N"
            ELSE
            /*/Consignment/PlaceOfUnloading = "O"
  </td>
</tr>


</table>
## CONDITION C0215

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC141C/Enquiry/text is PRESENT
            THEN
            IF /CC141C/CustomsOfficeOfDestinationActual is PRESENT
            THEN /CC141C/Consignment = "O"
            ELSE /CC141C/Consignment = "R"
            ELSE /CC141C/CustomsOfficeOfDestinationActual = "N"
            AND /CC141C/Consignment = "N"
  </td>
</tr>


</table>
## CONDITION C0220

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC141C/Enquiry/TC11DeliveryDate is PRESENT
            THEN /CC141C/Enquiry/text = "R"
            ELSE /CC141C/Enquiry/text = "O"
  </td>
</tr>


</table>
## CONDITION C0240

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Incident/code is EQUAL to ‘2’
            THEN /*/Consignment/Incident/TransportEquipment = "R" AND
            /*/Consignment/Incident/Transhipment = "O"
            ELSE IF /*/Incident/code is in SET { 3, 6}
            THEN /*/Consignment/Incident/TransportEquipment = "O" AND
            /*/Consignment/Incident/Transhipment = "R"
            ELSE
            /*/Consignment/Incident/TransportEquipment = "O" AND
            /*/ Consignment/Incident/Transhipment = "O"
  </td>
</tr>


</table>
## CONDITION C0250

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   F identificationNumber is PRESENT in this data group AND this identificationNumber is a valid identifier registered in the national Trader identification number register
            THEN
            name="O" AND Address="O"
            ELSE
            name="R" AND Address="R"
  </td>
</tr>


</table>
## CONDITION C0298

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/quantity&gt; is PRESENT
            THEN  /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/measurementUnitAndQualifier = "R"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/measurementUnitAndQualifier = "N"
  </td>
</tr>


</table>
## CONDITION C0315

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC141C/ENQUIRY/TC11DeliveryDate is PRESENT
            THEN /CC141C/CustomsOfficeOfDestinationActual = "R"
            ELSE /CC141C/CustomsOfficeOfDestinationActual= "O"
  </td>
</tr>


</table>
## CONDITION C0337

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/TransportCharges is PRESENT
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/TransportCharges = "N"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/TransportCharges = "O"
  </td>
</tr>


</table>
## CONDITION C0343

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/countryOfDestination is PRESENT
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination = "N"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination = "R"
  </td>
</tr>


</table>
## CONDITION C0349

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/Consignor is PRESENT
            THEN
            /*/Consignment/HouseConsignment/Consignor = "N"
            ELSE
            /*/Consignment/HouseConsignment/Consignor = "O"
  </td>
</tr>


</table>
## CONDITION C0382

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/LocationOfGoods/PostcodeAddress/country is in SET CL198
            THEN /*/Consignment/LocationOfGoods/PostcodeAddress/houseNumber = ''O''
            ELSE /*/Consignment/LocationOfGoods/PostcodeAddress/houseNumber = ''R''
  </td>
</tr>


</table>
## CONDITION C0387

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/PlaceOfLoading/UNLocode is PRESENT
            THEN /*/Consignment/PlaceOfLoading/country = "O" AND
            /*/Consignment/PlaceOfLoading/location = "O"
            ELSE /*/Consignment/PlaceOfLoading/country = "R" AND
            /*/Consignment/PlaceOfLoading/location = "R";

            IF /*/Consignment/PlaceOfUnloading/UNLocode is PRESENT
            THEN /*/Consignment/PlaceOfUnloading/country = "O" AND
            /*/Consignment/PlaceOfUnloading/location = "O"
            ELSE /*/Consignment/PlaceOfUnloading/country = "R" AND
            /*/Consignment/PlaceOfUnloading/location = "R"
  </td>
</tr>


</table>
## CONDITION C0394

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'Z'
            THEN
            /*/Consignment/LocationOfGoods/Address = "R"
            AND /*/Consignment/LocationOfGoods/authorisationNumber = "N"
            AND /*/Consignment/LocationOfGoods/UNLocode = "N"
            AND /*/Consignment/LocationOfGoods/CustomsOffice = "N"
            AND /*/Consignment/LocationOfGoods/GNSS = "N"
            AND /*/Consignment/LocationOfGoods/EconomicOperator = "N"
            AND /*/Consignment/LocationOfGoods/ContactPerson = "O"
            AND /*/Consignment/LocationOfGoods/PostcodeAddress = "N"
            ELSE IF /*/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'X'
            THEN
            /*/Consignment/LocationOfGoods/EconomicOperator = "R"
            AND /*/Consignment/LocationOfGoods/UNLocode = "N"
            AND /*/Consignment/LocationOfGoods/CustomsOffice = "N"
            AND /*/Consignment/LocationOfGoods/GNSS = "N"
            AND /*/Consignment/LocationOfGoods/authorisationNumber = "N"
            AND /*/Consignment/LocationOfGoods/Address = "N"
            AND /*/Consignment/LocationOfGoods/ContactPerson = "O"
            AND /*/Consignment/LocationOfGoods/PostcodeAddress = "N"
            ELSE IF /*/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'Y'
            THEN
            /*/Consignment/LocationOfGoods/authorisationNumber = "R"
            AND /*/Consignment/LocationOfGoods/UNLocode = "N"
            AND /*/Consignment/LocationOfGoods/CustomsOffice = "N"
            AND /*/Consignment/LocationOfGoods/GNSS = "N"
            AND /*/Consignment/LocationOfGoods/EconomicOperator = "N"
            AND /*/Consignment/LocationOfGoods/Address = "N"
            AND /*/Consignment/LocationOfGoods/ContactPerson = "O"
            AND /*/Consignment/LocationOfGoods/PostcodeAddress = "N"
            ELSE IF /*/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'W'
            THEN
            /*/Consignment/LocationOfGoods/GNSS = "R"
            AND /*/Consignment/LocationOfGoods/UNLocode = "N"
            AND /*/Consignment/LocationOfGoods/CustomsOffice = "N"
            AND /*/Consignment/LocationOfGoods/EconomicOperator = "N"
            AND /*/Consignment/LocationOfGoods/authorisationNumber = "N"
            AND /*/Consignment/LocationOfGoods/Address = "N"
            AND /*/Consignment/LocationOfGoods/ContactPerson = "O"
            AND /*/Consignment/LocationOfGoods/PostcodeAddress = "N"
            ELSE IF /*/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'V'
            THEN
            /*/Consignment/LocationOfGoods/CustomsOffice = "R"
            AND /*/Consignment/LocationOfGoods/UNLocode = "N"
            AND /*/Consignment/LocationOfGoods/GNSS = "N"
            AND /*/Consignment/LocationOfGoods/EconomicOperator = "N"
            AND /*/Consignment/LocationOfGoods/authorisationNumber = "N"
            AND /*/Consignment/LocationOfGoods/Address = "N"
            AND /*/Consignment/LocationOfGoods/ContactPerson = "N"
            AND /*/Consignment/LocationOfGoods/PostcodeAddress = "N"
            ELSE IF /*/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'U'
            THEN
            /*/Consignment/LocationOfGoods/UNLocode = "R"
            AND/*/Consignment/LocationOfGoods/CustomsOffice = "N"
            AND/*/Consignment/LocationOfGoods/GNSS = "N"
            AND/*/Consignment/LocationOfGoods/authorisationNumber = "N"
            AND/*/Consignment/LocationOfGoods/EconomicOperator = "N"
            AND/*/Consignment/LocationOfGoods/Address = "N"
            AND /*/Consignment/LocationOfGoods/ContactPerson = "O"
            AND /*/Consignment/LocationOfGoods/PostcodeAddress = "N"
            ELSE IF /*/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'T'
            THEN
            /*/Consignment/LocationOfGoods/Address = "N"
            AND /*/Consignment/LocationOfGoods/authorisationNumber = "N"
            AND /*/Consignment/LocationOfGoods/UNLocode = "N"
            AND /*/Consignment/LocationOfGoods/CustomsOffice = "N"
            AND /*/Consignment/LocationOfGoods/GNSS = "N"
            AND /*/Consignment/LocationOfGoods/EconomicOperator = "N"
            AND /*/Consignment/LocationOfGoods/ContactPerson = "O"
            AND /*/Consignment/LocationOfGoods/PostcodeAddress = "R"
  </td>
</tr>


</table>
## CONDITION C0396

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/Incident/code is EQUAL to ‘2’
            THEN /*/Consignment/Incident/TransportEquipment/numberOfSeals = "R"
            ELSE /*/Consignment/Incident/TransportEquipment/numberOfSeals = "O"
  </td>
</tr>


</table>
## CONDITION C0397

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/Incident/code is in SET {3, 6}
            THEN /*/Consignment/Incident/Transhipment/TransportMeans = "R"
            ELSE /*/Consignment/Incident/Transhipment/TransportMeans = "O"
  </td>
</tr>


</table>
## CONDITION C0399

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/reducedDatasetIndicator IS EQUAL TO '1'
            THEN
            /*/Consignment/inlandModeOfTransport = "N"
            ELSE
            /*/Consignment/inlandModeOfTransport = "O"
  </td>
</tr>


</table>
## CONDITION C0403

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/additionalDeclarationType is EQUAL to “D”
            THEN /*/Consignment/PlaceOfLoading = “O”
            ELSE /*/Consignment/PlaceOfLoading = “R”
  </td>
</tr>


</table>
## CONDITION C0404

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF (/CC015C/Consignment/PlaceOfLoading is PRESENT OR /CC013C/Consignment/PlaceOfLoading is PRESENT)
            THEN /CC170C/Consignment/PlaceOfLoading = “O”
            ELSE /CC170C/Consignment/PlaceOfLoading = “R”
  </td>
</tr>

</table>
## CONDITION C0411

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to 'TIR'   (and to 'TIRME')
            THEN /*/TransitOperation/TIRCarnetNumber = "R"
            ELSE /*/TransitOperation/TIRCarnetNumber = "N"
  </td>
</tr>


</table>
## CONDITION C0440

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC043C/Consignment/TransportEquipment/numberOfSeals &gt; is EQUAL to '0'
            OR /CC043C/Consignment/Incident/TransportEquipment/numberOfSeals &gt; is EQUAL to '0'
            THEN /CC044C/UnloadingRemark/stateOfSeals = "R"
            ELSE /CC044C/UnloadingRemark/stateOfSeals = "N"
  </td>
</tr>


</table>
## CONDITION C0460

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'W'
            THEN
            /*/Consignment/Incident/Location/GNSS = "R" AND
            /*/Consignment/Incident/Location/UNLocode = "N" AND
            /*/Consignment/Incident/Location/Address = "N"
            ELSE IF /*/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'U'
            THEN
            /*/Consignment/Incident/Location/UNLocode = "R" AND
            /*/Consignment/Incident/Location/GNSS = "N" AND
            /*/Consignment/Incident/Location/Address = "N"
            ELSE IF /*/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'Z'
            THEN
            /*/Consignment/Incident/Location/Address = "R" AND
            /*/Consignment/Incident/Location/UNLocode = "N" AND
            /*/Consignment/Incident/Location/GNSS = "N"
  </td>
</tr>


</table>
## CONDITION C0467

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC028C/TransitOperation/declarationAcceptanceDate&gt; is PRESENT
            THEN
            /*/TransitOperation/MRN = "R" AND
            /*/TransitOperation/LRN = "N"
            ELSE /*/TransitOperation/MRN = "N" AND
            /*/TransitOperation/LRN = "R"
  </td>
</tr>


</table>
## CONDITION C0502

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/referenceNumberUCR is PRESENT
            THEN /*/Consignment/HouseConsignment/referenceNumberUCR = "N" AND
            /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "N"
            ELSE
            IF /*/Consignment/HouseConsignment/referenceNumberUCR is PRESENT
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "N"
            ELSE
            IF (/*/Consignment/TransportDocument is PRESENT OR
            /*/Consignment/HouseConsignment/TransportDocument is PRESENT)
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "O"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "R"
  </td>
</tr>


</table>
## CONDITION C0505

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/HolderOfTheTransitProcedure/Address/country is in SET CL505
            THEN /*/HolderOfTheTransitProcedure/Address/postcode = "O"
            ELSE /*/HolderOfTheTransitProcedure/Address/postcode = "R";

            IF /*/Consignment/Consignor/Address/country is in SET CL505
            THEN /*/Consignment/Consignor/Address/postcode = "O"
            ELSE /*/Consignment/Consignor/Address/postcode = "R";

            IF /*/Consignment/Consignee/Address/country is in SET CL505
            THEN /*/Consignment/Consignee/Address/postcode = "O"
            ELSE /*/Consignment/Consignee/Address/postcode = "R";

            IF /*/Consignment/Incident/Location/country is in SET CL505
            THEN /*/Consignment/Incident/Location/Address/postcode = "O"
            ELSE /*/Consignment/Incident/Location/Address/postcode = "R";

            IF /*/Consignment/LocationOfGoods/Address/country is in SET CL505
            THEN /*/Consignment/LocationOfGoods/Address/postcode = "O"
            ELSE /*/Consignment/LocationOfGoods/Address/postcode = "R";

            IF /*/Consignment/HouseConsignment/Consignor/Address/country is in SET CL505
            THEN /*/Consignment/HouseConsignment/Consignor/Address/postcode = "O"
            ELSE /*/Consignment/HouseConsignment/Consignor/Address/postcode = "R";

            IF /*/Consignment/HouseConsignment/Consignee/Address/country is in SET CL505
            THEN /*/Consignment/HouseConsignment/Consignee/Address/postcode = "O"
            ELSE /*/Consignment/HouseConsignment/Consignee/Address/postcode = "R";

            IF /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/country is in SET CL505
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/postcode = "O"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/postcode = "R";

            IF /*/Guarantor/Address/country is in SET CL505
            THEN /*/Guarantor/Address/postcode = "O"
            ELSE /*/Guarantor/Address/postcode = "R";

            IF /*/GuaranteeReference/Guarantor/Address/country is in SET CL505
            THEN /*/GuaranteeReference/Guarantor/Address/postcode = "O"
            ELSE /*/GuaranteeReference/Guarantor/Address/postcode = "R";

            IF /*/GuaranteeReference/Owner/Address/country is in SET CL505
            THEN /*/GuaranteeReference/Owner/Address/postcode = "O"
            ELSE /*/GuaranteeReference/Owner/Address/postcode = "R";

            IF /*/Consignment/ConsigneeActual/Address/country is in SET CL505
            THEN /*/Consignment/ConsigneeActual/Address/postcode = "O"
            ELSE /*/Consignment/ConsigneeActual/Address/postcode = "R"
  </td>
</tr>


</table>
## CONDITION C0505_Incident

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/HolderOfTheTransitProcedure/Address/country is in SET CL505
            THEN /*/HolderOfTheTransitProcedure/Address/postcode = "O"
            ELSE /*/HolderOfTheTransitProcedure/Address/postcode = "R";

            IF /*/Consignment/Consignor/Address/country is in SET CL505
            THEN /*/Consignment/Consignor/Address/postcode = "O"
            ELSE /*/Consignment/Consignor/Address/postcode = "R";

            IF /*/Consignment/Consignee/Address/country is in SET CL505
            THEN /*/Consignment/Consignee/Address/postcode = "O"
            ELSE /*/Consignment/Consignee/Address/postcode = "R";

            IF /*/Consignment/Incident/Location/country is in SET CL505
            THEN /*/Consignment/Incident/Location/Address/postcode = "O"
            ELSE /*/Consignment/Incident/Location/Address/postcode = "R";

            IF /*/Consignment/LocationOfGoods/Address/country is in SET CL505
            THEN /*/Consignment/LocationOfGoods/Address/postcode = "O"
            ELSE /*/Consignment/LocationOfGoods/Address/postcode = "R";

            IF /*/Consignment/HouseConsignment/Consignor/Address/country is in SET CL505
            THEN /*/Consignment/HouseConsignment/Consignor/Address/postcode = "O"
            ELSE /*/Consignment/HouseConsignment/Consignor/Address/postcode = "R";

            IF /*/Consignment/HouseConsignment/Consignee/Address/country is in SET CL505
            THEN /*/Consignment/HouseConsignment/Consignee/Address/postcode = "O"
            ELSE /*/Consignment/HouseConsignment/Consignee/Address/postcode = "R";

            IF /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/country is in SET CL505
            THEN /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/postcode = "O"
            ELSE /*/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/postcode = "R";

            IF /*/Guarantor/Address/country is in SET CL505
            THEN /*/Guarantor/Address/postcode = "O"
            ELSE /*/Guarantor/Address/postcode = "R";

            IF /*/GuaranteeReference/Guarantor/Address/country is in SET CL505
            THEN /*/GuaranteeReference/Guarantor/Address/postcode = "O"
            ELSE /*/GuaranteeReference/Guarantor/Address/postcode = "R";

            IF /*/GuaranteeReference/Owner/Address/country is in SET CL505
            THEN /*/GuaranteeReference/Owner/Address/postcode = "O"
            ELSE /*/GuaranteeReference/Owner/Address/postcode = "R";

            IF /*/Consignment/ConsigneeActual/Address/country is in SET CL505
            THEN /*/Consignment/ConsigneeActual/Address/postcode = "O"
            ELSE /*/Consignment/ConsigneeActual/Address/postcode = "R"
  </td>
</tr>

</table>
## CONDITION C0531

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/security is in SET {1,2,3}
            AND /*/Consignment/modeOfTransportAtTheBorder is EQUAL to ‘4’
            THEN /*/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber = "R"
            ELSE /*/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber = "O"
  </td>
</tr>


</table>
## CONDITION C0542

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/security is EQUAL to '0' AND /*/TransitOperation/reducedDatasetIndicator is EQUAL to '1'
            THEN
            /*/Consignment/Consignor = "N" AND /*/Consignment/HouseConsignment/Consignor = "N"
            ELSE
            IF /*/Consignment/Consignor is PRESENT
            THEN /*/Consignment/HouseConsignment/Consignor = "N"
            ELSE /*/Consignment/HouseConsignment/Consignor = "O"
  </td>
</tr>


</table>
## CONDITION C0569

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/Incident/TransportEquipment/numberOfSeals is GREATER than '0'
            THEN
            /*/Consignment/Incident/TransportEquipment/Seal = "R"
            ELSE
            /*/Consignment/Incident/TransportEquipment/Seal = "N";

            IF /*/Consignment/TransportEquipment/numberOfSeals is GREATER than '0'
            THEN
            /*/Consignment/TransportEquipment/Seal = "R"
            ELSE
            /*/Consignment/TransportEquipment/Seal = "N"
  </td>
</tr>


</table>
## CONDITION C0586

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/bindingItinerary is EQUAL to ‘1’
            THEN /*/Consignment/CountryOfRoutingOfConsignment = "R"
            ELSE /*/Consignment/CountryOfRoutingOfConsignment = "O"
  </td>
</tr>


</table>
## CONDITION C0587

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/security is in SET {2, 3}
            THEN /*/CustomsOfficeOfExitForTransitDeclared = "O"
            ELSE /*/CustomsOfficeOfExitForTransitDeclared = "N"
  </td>
</tr>


</table>
## CONDITION C0598

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/security is in SET {1, 3} AND
            the first two characters of the /*/CustomsOfficeOfTransitDeclared/referenceNumber is in SET CL147
            THEN /*/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated ="R"
            ELSE /*/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated = "O"
  </td>
</tr>


</table>
## CONDITION C0599

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/security is in SET {1,2,3} AND
            /*/TransitOperation/additionalDeclarationType is EQUAL to ‘A’
            THEN /*/Consignment/modeOfTransportAtTheBorder = "R"
            ELSE /*/Consignment/modeOfTransportAtTheBorder = "O"
  </td>
</tr>


</table>
## CONDITION C0600

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF  (/CC013C/TransitOperation/security is in SET {1,2,3}) OR (/CC015C/TransitOperation/security is in SET {1,2,3})
            THEN
            /CC170C/Consignment/modeOfTransportAtTheBorder = "R"
            ELSE /CC170C/Consignment/modeOfTransportAtTheBorder = "O"
  </td>
</tr>


</table>
## CONDITION C0670

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/TransportEquipment is PRESENT only once AND /*/Consignment/TransportEquipment/containerIdentificationNumber is PRESENT
            THEN /*/Consignment/TransportEquipment/GoodsReference = "O"
            ELSE /*/Consignment/TransportEquipment/GoodsReference = "R"
  </td>
</tr>


</table>
## CONDITION C0671

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/LocationOfGoods/EconomicOperator/identificationNumber is PRESENT
            OR /*/Consignment/LocationOfGoods/authorisationNumber is PRESENT
            THEN /*/Consignment/LocationOfGoods/additionalIdentifier = "O"
            ELSE /*/Consignment/LocationOfGoods/additionalIdentifier = "N"
  </td>
</tr>


</table>
## CONDITION C0710

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/Additional declaration type&gt; is EQUAL to 'D'
            THEN /*/Consignment/LocationOfGoods = "O"
            ELSE IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in SET CL147
            THEN /*/Consignment/LocationOfGoods = "O"
            ELSE /*/Consignment/LocationOfGoods = "R"
  </td>
</tr>


</table>
## CONDITION C0806

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/modeOfTransportAtTheBorder is EQUAL to '5'
            THEN /*/Consignment/ActiveBorderTransportMeans = “N”
            ELSE
            IF (/*/TransitOperation/security is in SET {1,2,3} AND
            /*/TransitOperation/additionalDeclarationType is EQUAL to ‘A’)
            THEN /*/Consignment/ActiveBorderTransportMeans = “R”
            ELSE /*/Consignment/ActiveBorderTransportMeans = “O”
  </td>
</tr>


</table>
## CONDITION C0820

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/Incident/Transhipment/containerIndicator is EQUAL to '1' 
            THEN
            /*/Consignment/Incident/TransportEquipment/containerIdentificationNumber = "R"
            ELSE
            /*/Consignment/Incident/TransportEquipment/containerIdentificationNumber = "O"
  </td>
</tr>


</table>
## CONDITION C0821

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF the first two characters of /*/CustomsOfficeOfDeparture/referenceNumber is in SET CL112
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomenclatureCode = "N"
            ELSE
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl
            atureCode = "O".
  </td>
</tr>


</table>
## CONDITION C0822

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/additionalDeclarationType is EQUAL to 'D'
            THEN /*/Consignment/containerIndicator = "O"
            ELSE /*/Consignment/containerIndicator = "R"
  </td>
</tr>


</table>
## CONDITION C0823

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/containerIndicator is PRESENT
            THEN
            IF /*/Consignment/containerIndicator is EQUAL to ‘1’
            THEN /*/Consignment/TransportEquipment = "R"
            ELSE /*/Consignment/TransportEquipment = "O"
            ELSE /*/Consignment/TransportEquipment = "N"
  </td>
</tr>


</table>
## CONDITION C0824

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC015C/Consignment/containerIndicator AND /CC013C/Consignment/containerIndicator is PRESENT
            THEN /CC170C/Consignment/containerIndicator = "O"
            ELSE /CC170C/Consignment/containerIndicator = "R"
  </td>
</tr>


</table>
## CONDITION C0826

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/inlandModeOfTransport is EQUAL to '5'
            THEN
            /*/Consignment/DepartureTransportMeans = “N” AND /*/Consignment/HouseConsignment/DepartureTransportMeans = "N"
            ELSE
            IF /*/Consignment/DepartureTransportMeans is PRESENT
            THEN /*/Consignment/HouseConsignment/DepartureTransportMeans = "N"
            ELSE /*/Consignment/HouseConsignment/DepartureTransportMeans = "O"
  </td>
</tr>


</table>
## CONDITION C0833

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/inlandModeOfTransport is EQUAL to '5'
            THEN
            /CC170C/Consignment/DepartureTransportMeans = “N” AND
            /CC170C/Consignment/HouseConsignment/DepartureTransportMeans = “N”
            ELSE
            IF /CC015C/Consignment/DepartureTransportMeans is NOT PRESENT AND
            /CC015C/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT AND  /CC013C/Consignment/DepartureTransportMeans is NOT PRESENT AND
            /CC013C/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT
            THEN
            IF /CC170C/Consignment/DepartureTransportMeans is PRESENT
            THEN /CC170C/Consignment/HouseConsignment/DepartureTransportMeans = "N"
            ELSE /CC170C/Consignment/HouseConsignment/DepartureTransportMeans = "O"
  </td>
</tr>


</table>
## CONDITION C0837

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Consignment/HouseConsignment/PreviousDocument/ is PRESENT
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/ GoodsMeasure ="R"
            AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "R"
            ELSE IF /*/ TransitOperation/reducedDatasetIndicator is EQUAL TO ‘1’
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure = "O"
            AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "N"
            ELSE
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure ="O"
            AND
            /*/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "O"
  </td>
</tr>


</table>
## CONDITION C0839

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/Authorisation/type is NOT EQUAL to 'C521'
            THEN
            /*/TransitOperation/limitDate = “N”
            ELSE
            IF /*/TransitOperation/additionalDeclarationType is EQUAL to 'D'
            THEN
            /*/TransitOperation/limitDate = “O”
            ELSE
            /*/TransitOperation/limitDate = “R”
  </td>
</tr>


</table>
## CONDITION C0840

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /CC015C/Authorisation/type is NOT EQUAL to 'C521' OR /CC013C/Authorisation/type is NOT EQUAL to 'C521'
            THEN /CC170C/TransitOperation/limitDate = “N”
            ELSE
            IF /CC015C/TransitOperation/limitDate is NOT PRESENT AND /CC013C/TransitOperation/limitDate is NOT PRESENT
            THEN /CC170C/TransitOperation/limitDate = “R”
            ELSE /CC170C/TransitOperation/limitDate = “O”
  </td>
</tr>


</table>
## CONDITION C0904

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is PRESENT
            THEN IF /*/TransitOperation/declarationType is EQUAL to 'TIR'
            THEN /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "R"
            ELSE /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "N"
            ELSE IF /CC015C/TransitOperation/declarationType is EQUAL to 'TIR' OR
            /CC013C/TransitOperation/declarationType is EQUAL to 'TIR'
            THEN /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "R"
            ELSE /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "N"

            IF /*/TransitOperation/declarationType is PRESENT
            THEN IF /*/TransitOperation/declarationType is EQUAL to 'TIR'
            THEN /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "R"
            ELSE /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "N"
            ELSE IF /CC015C/TransitOperation/declarationType is EQUAL to 'TIR' OR
            /CC013C/TransitOperation/declarationType is EQUAL to 'TIR'
            THEN /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "R"
            ELSE /*/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "N"
  </td>
</tr>


</table>
## CONDITION C0909

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to 'TIR'
            THEN
            IF /*/Consignment/countryOfDispatch is PRESENT
            THEN
            /*/Consignment/HouseConsignment/countryOfDispatch = "N" AND
            /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"
            ELSE
            IF /*/Consignment/HouseConsignment/countryOfDispatch is PRESENT
            THEN
            /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"
            ELSE
            /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "R"
            ELSE
            /*/Consignment/countryOfDispatch= "N" AND
            /*/Consignment/HouseConsignment/countryOfDispatch = "N" AND
            /*/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"
  </td>
</tr>


</table>
## CONDITION CN001

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is in SET  {T1ME, TIRME, ATA, SCDIM, SCDEX}
            THEN /*/CustomsOfficeOfTransitDeclared = "N"
            ELSE /*/CustomsOfficeOfTransitDeclared = "R"
  </td>
</tr>


</table>
## CONDITION CN002

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is in SET   {T1ME, T2ME, TIRME, ATA, SCDIM, SCDEX}
            THEN /*/CustomsOfficeOfExitForTransitDeclared = "N"
            ELSE /*/CustomsOfficeOfExitForTransitDeclared = "O"
  </td>
</tr>


</table>
## CONDITION CN003

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to  'TIR' or 'TIRME'
            THEN /*/TransitOperation/TIRValidityDate = "R"
            ELSE /*/TransitOperation/TIRValidityDate = "N"
  </td>
</tr>


</table>
## CONDITION CN004

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   D.I. must be used IF /*/TransitOperation/declarationType is NOT EQUAL to 'TIR' or  'TIRME'
            and at the same CONSIGNMENT ITEM/Item price (EUR) “ is not used.
  </td>
</tr>


</table>
## CONDITION CN005

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF /*/TransitOperation/declarationType is EQUAL to 'TIR' or 'TIRME'
            THEN this element cannot be used
            ELSE this element can be used
  </td>
</tr>


</table>
## CONDITION CN006

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   D.I. (Data Item) must be used when is declared Excise goods (CLEXCISE)
  </td>
</tr>


</table>
## CONDITION CN007

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   D.I. must be used when GUARANTEE/Guarantee type is in SET (0,1,2,4,9)
  </td>
</tr>


</table>
## CONDITION CN008

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   D.I. must be used when UnloadingRemark/Conform is false
  </td>
</tr>

</table>
## CONDITION CN109

<table class="table width-min-100">
<tr>
<td class="label">
   Description
  </td>
<td class="description">
   IF TransitOperation.FallbackProcedure is true THEN the element SHALL be used ELSE the element CANNOT be used.
  </td>
</tr>

</table>
