## C0001

**Functional Description**

IF &lt;CONSIGNMENT.Country of destination&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
THEN<br />
IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br />
THEN<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; = "N"<br />
  ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; ="R"<br />
ELSE IF &lt;TRANSIT OPERATION.Security&gt; is in SET {0,1}<br />
THEN<br />
   IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br />
  THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; = "N"<br />
 ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT -CONSIGNEE&gt;= "O"<br />
ELSE<br />
  IF &lt;CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; is EQUAL to '30600'<br />
  THEN<br />
 &lt;CONSIGNMENT-CONSIGNEE&gt; = "N" AND<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL INFORMATION.Code&gt; is EQUAL<br />
to '30600'<br />
THEN<br />
 &lt;CONSIGNMENT-CONSIGNEE&gt; = "N" AND<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; = "N"<br />
ELSE<br />
   IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br />
   THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; = "N"<br />
  ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
THEN<br />
 IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br />
 THEN<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "N"<br />
   ELSE /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "R"<br />
ELSE IF /<span>&#42;</span>/TransitOperation/security is in SET {0,1}<br />
THEN<br />
 IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br />
 THEN<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "O"<br />
ELSE IF at least one instance of /<span>&#42;</span>/Consignment/AdditionalInformation/code is EQUAL to '30600'<br />
  THEN<br />
  /<span>&#42;</span>/Consignment/Consignee = "N" AND<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "N"<br />
ELSE IF at least one instance of /<span>&#42;</span>/Consignment/HouseConsignment/AdditionalInformation/code IS<br />
EQUAL to '30600'<br />
THEN<br />
   /<span>&#42;</span>/Consignment/Consignee = "N" AND<br />
   THIS /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "N"<br />
ELSE<br />
  IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br />
 THEN<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/Consignee = "R"


## C0002

**Functional Description**

IF &lt;CD001C- CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br />
 THEN &lt;CD012C- CONSIGNMENT-CONSIGNEE&gt; = "R" AND<br />
  &lt;CD012C- CONSIGNMENT-HOUSE CONSIGNMENT -CONSIGNEE&gt; = "N"<br />
ELSE IF &lt;CD001C- CONSIGNMENT-HOUSE CONSIGNMENT -CONSIGNEE&gt; is PRESENT<br />
  THEN &lt;CD012C- CONSIGNMENT-HOUSE CONSIGNMENT -CONSIGNEE&gt; = "R" AND<br />
  &lt;CD012C- CONSIGNMENT-CONSIGNEE&gt; = "N"<br />
ELSE &lt;CD012C- CONSIGNMENT-CONSIGNEE&gt; = "N” AND<br />
  &lt;CD012C- CONSIGNMENT-HOUSE CONSIGNMENT -CONSIGNEE&gt; = "N"

**Technical Description**

IF /CD001C/Consignment/Consignee is PRESENT<br />
  THEN /CD012C/Consignment/Consignee = "R" AND<br />
  /CD012C/Consignment/HouseConsignment/Consignee = "N"<br />
ELSE IF /CD001C/Consignment/HouseConsignment/Consignee is PRESENT<br />
  THEN /CD012C/Consignment/HouseConsignment/Consignee = "R" AND<br />
  /CD012C/Consignment/Consignee = "N"<br />
ELSE /CD012C/Consignment/Consignee = "N” AND<br />
  /CD012C/Consignment/HouseConsignment/Consignee = "N"


## C0004

**Functional Description**

IF the recovery request message is sent by country of departure AND<br />
&lt;CC029C-GUARANTEE.Guarantee type&gt; is in SET {1, 2, 4, 9}<br />
THEN &lt;CD150C-GUARANTEE REFERENCE&gt; = "R"<br />
ELSE &lt;CD150C-GUARANTEE REFERENCE&gt; = "O"

**Technical Description**

IF the recovery request message is sent by country of departure AND<br />
/CC029C/Guarantee/guaranteeType is in SET {1, 2, 4, 9}<br />
THEN /CD150C/GuaranteeReference = "R"<br />
ELSE /CD150C/GuaranteeReference = "O"


## C0009

**Functional Description**

IF &lt;CC141C-CONSIGNMENT&gt; is PRESENT<br />
THEN &lt;CD142C-CONSIGNMENT&gt; = "R"<br />
ELSE &lt;CD142C-CONSIGNMENT&gt; = "N"

**Technical Description**

IF /CC141C/Consignment is PRESENT<br />
THEN /CD142C/Consignment = "R"<br />
ELSE /CD142C/Consignment = "N"


## C0012

**Functional Description**

IF &lt;ENQUIRY.Response Code&gt; is EQUAL to '3'<br />
THEN &lt;CD143C-ENQUIRY.Return copy returned date&gt; = "R"<br />
ELSE &lt;CD143C-ENQUIRY.Return copy returned date&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Enquiry/responseCode is EQUAL to '3'<br />
THEN /CD143C/Enquiry/returnCopyReturnedDate = "R"<br />
ELSE /CD143C/Enquiry/returnCopyReturnedDate = "N"


## C0013

**Functional Description**

IF &lt;ENQUIRY.Response Code&gt; is in SET {2, 4}<br />
THEN &lt;CD143C-ENQUIRY.Text&gt; = "R"<br />
ELSE &lt;CD143C-ENQUIRY.Text&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Enquiry/responseCode is in SET {2, 4}<br />
THEN /CD143C/Enquiry/text = "R"<br />
ELSE /CD143C/Enquiry/text = "N"


## C0014

**Functional Description**

IF the last two characters of &lt;Message sender&gt; are EQUAL to the 3rd and 4rth character of<br />
&lt;GUARANTEE REFERENCE.GRN&gt; AND<br />
IF &lt;CD205C-GUARANTEE.Guarantee type&gt; is in SET {1, 2, 4, 9}<br />
THEN &lt;GUARANTEE REFERENCE-GUARANTOR&gt; = "R"<br />
ELSE &lt;GUARANTEE REFERENCE -GUARANTOR&gt; = "O"

**Technical Description**

IF the last two characters of /<span>&#42;</span>/messageSender are EQUAL to the 3rd and 4rth character of<br />
/<span>&#42;</span>/GuaranteeReference/GRN AND<br />
IF /CD205C/Guarantee/guaranteeType is in SET {1, 2, 4, 9}<br />
THEN /<span>&#42;</span>/GuaranteeReference/Guarantor = "R"<br />
ELSE /<span>&#42;</span>/GuaranteeReference/Guarantor = "O"


## C0015

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br />
REFERENCE.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a> (DocumentTypeExcise)<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br />
REFERENCE.Reference number&gt; = “R”<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br />
REFERENCE.Reference number&gt; = “O”

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/type is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a>(DocumentTypeExcise)<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/referenceNumber =<br />
“R”<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/referenceNumber =<br />
“O”


## C0025

**Functional Description**

IF the recovery acceptance notification is sent by the country of departure AND<br />
&lt;RECOVERY.Recovery acceptance&gt; flag is EQUAL to '1' AND &lt;CC029C-GUARANTEE.Guarantee<br />
type&gt; is in SET {1, 2, 4, 9}<br />
THEN &lt;CD151C-GUARANTEE REFERENCE&gt; = "R"<br />
ELSE &lt;CD151C-GUARANTEE REFERENCE&gt; = "O"

**Technical Description**

IF the recovery acceptance notification is sent by the country of departure AND<br />
/<span>&#42;</span>/Recovery/recoveryAcceptance flag is EQUAL to '1' AND /CC029C/Guarantee/guaranteeType is in<br />
SET {1, 2, 4, 9}<br />
THEN /CD151C/GuaranteeReference = "R"<br />
ELSE /CD151C/GuaranteeReference = "O"


## C0027

**Functional Description**

IF &lt;CTL control&gt; is PRESENT<br />
THEN<br />
&lt;CC043C-HOLDER OF THE TRANSIT PROCEDURE&gt; = "N"<br />
AND &lt;CC043C-CONSIGNMENT&gt; = "N"<br />
AND &lt;CC043C-TRANSIT OPERATION.Declaration type&gt; = "N"<br />
AND &lt;CC043C-TRANSIT OPERATION.Declaration acceptance date&gt; = "N"<br />
AND &lt;CC043C-CONSIGNMENT.Gross mass&gt; = "N"<br />
ELSE<br />
&lt;CC043C-HOLDER OF THE TRANSIT PROCEDURE&gt; = "R"<br />
AND &lt;CC043C-CONSIGNMENT&gt; = "R"<br />
AND &lt;CC043C-TRANSIT OPERATION.Declaration type&gt; = "R"<br />
AND &lt;CC043C-TRANSIT OPERATION.Declaration acceptance date&gt; = "R"<br />
AND &lt;CC043C-CONSIGNMENT.Gross mass&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/CTLControl is PRESENT<br />
THEN /CC043C/HolderOfTheTransitProcedure = "N" AND<br />
/CC043C/Consignment = "N" AND<br />
/CC043C/TransitOperation/declarationType = "N" AND<br />
/CC043C/TransitOperation/declarationAcceptanceDate = "N" AND<br />
/CC043C/Consignment/grossMass = "N"<br />
ELSE /CC043C/HolderOfTheTransitProcedure = "R" AND<br />
/CC043C/ Consignment = "R" AND<br />
/CC043C/TransitOperation/declarationType = "R" AND<br />
/CC043C/TransitOperation/declarationAcceptanceDate = "R" AND<br />
/CC043C/Consignment/grossMass = "R"


## C0029

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br />
THEN &lt;CONSIGNMENT.Mode of transport at the border&gt; = "R"<br />
ELSE &lt;CONSIGNMENT.Mode of transport at the border&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1,2,3}<br />
THEN /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder = "R"<br />
ELSE /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder = "O"


## C0030

**Functional Description**

IF &lt;TRANSIT OPERATION. Declaration type&gt; is in SET {TIR,T2SM}<br />
 THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "N"<br />
ELSE<br />
 IF (the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br />
 is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC)) AND (the first two characters of &lt;CUSTOMS OFFICE<br />
 OF DESTINATION (DECLARED). Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
 (CountryCodesCTC)) AND (the first two characters of &lt;CUSTOMS OFFICE OF<br />
 DEPARTURE.Reference number&gt; is EQUAL to the first two characters of CUSTOMS<br />
 OFFICE OF DESTINATION (DECLARED). Reference number&gt;)<br />
  THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "O"<br />
ELSE<br />
  IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'T2'<br />
   THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R"<br />
ELSE<br />
  IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL 'T' AND at least one instance of<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is<br />
  EQUAL to 'T2'<br />
THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R"<br />
ELSE<br />
   IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br />
   is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC) OR the first two characters of &lt;CUSTOMS OFFICE<br />
   OF DESTINATION (DECLARED). Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
   (CountryCodesCTC)<br />
THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R"<br />
ELSE<br />
   IF at least one instance of &lt;CONSIGNMENT-COUNTRY OF ROUTING OF<br />
CONSIGNMENT.Country&gt; is in<br />
   SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC)<br />
THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R"<br />
ELSE<br />
   IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br />
   is EQUAL to 'AD' OR IF the first two characters of &lt;CUSTOMS OFFICE OF<br />
   DESTINATION (DECLARED). Reference number&gt; is EQUAL to 'AD'<br />
THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R"<br />
ELSE<br />
   IF &lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; is PRESENT<br />
   THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "R"<br />
ELSE<br />
&lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is in SET {TIR,T2SM}<br />
 THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "N"<br />
ELSE<br />
 IF (the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET<br />
 <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a>) AND (the first two characters of<br />
 /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a>) AND (the first<br />
 two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to the first two<br />
 characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber)<br />
THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "O"<br />
ELSE<br />
 IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T2'<br />
 THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "R"<br />
ELSE<br />
 IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL 'T' AND at least one instance of<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is EQUAL to 'T2'<br />
 THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "R"<br />
ELSE<br />
 IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET<br />
 <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> OR the first two characters of<br />
 /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
 THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "R"<br />
ELSE<br />
 IF at least one instance of /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment/country is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
 THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "R"<br />
ELSE<br />
 IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to<br />
 'AD' OR IF the first two characters of<br />
 /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to 'AD'<br />
 THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "R"<br />
ELSE<br />
 IF /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared is PRESENT<br />
 THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "R"<br />
ELSE<br />
 /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "O"


## C0035

**Functional Description**

IF (&lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F}<br />
AND the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC))<br />
THEN IF &lt;CONSIGNMENT-PREVIOUS DOCUMENT&gt; is PRESENT<br />
   THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br />
   DOCUMENT&gt; = ‘O’<br />
   ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br />
   DOCUMENT&gt; = ‘R’<br />
   for all Consignment Items<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS DOCUMENT&gt;<br />
= ‘O’;<br />
IF (&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is in SET<br />
{T2, T2F} AND the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br />
is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC))<br />
THEN IF &lt;CONSIGNMENT-PREVIOUS DOCUMENT&gt; is PRESENT<br />
   THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br />
   DOCUMENT&gt; = ‘O’<br />
   ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br />
   DOCUMENT&gt; = ‘R’<br />
   for this Consignment Items<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS DOCUMENT&gt;<br />
= ‘O’ for this Consignment Items

**Technical Description**

IF (/<span>&#42;</span>/Transit Operation/declarationType is in SET {T2, T2F}<br />
AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a>)<br />
THEN IF /<span>&#42;</span>/Consignment/PreviousDocument is PRESENT<br />
   THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument = ‘O’<br />
   ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument = ‘R’<br />
   for all Consignment Items<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument = ‘O’;<br />
IF (/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2, T2F} AND<br />
the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a>)<br />
THEN IF /<span>&#42;</span>/Consignment/PreviousDocument is PRESENT<br />
   THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument = ‘O’<br />
   ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument = ‘R’<br />
   for this Consignment Items<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument = ‘O’<br />
for this Consignment Items


## C0040

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is EQUAL to '1'<br />
THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT &gt; = "R"<br />
ELSE<br />
&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/Transhipment/containerIndicator is EQUAL to '1'<br />
THEN<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment = "O"


## C0045

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to ‘T’<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; = "R"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T'<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType = "R"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType = "N"


## C0055

**Functional Description**

IF &lt;CONSIGNMENT.Container indicator&gt; is EQUAL to '0'<br />
THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Container identification number&gt; = "N"<br />
ELSE at least one iteration of &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Container identification<br />
number&gt; = "R" (for the rest of iterations is optional)

**Technical Description**

IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to '0'<br />
THEN /<span>&#42;</span>/Consignment/TransportEquipment/containerIdentificationNumber = "N"<br />
ELSE at least one iteration of /<span>&#42;</span>/Consignment/TransportEquipment/containerIdentificationNumber = "R"<br />
(for the rest of iterations is optional)


## C0060

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of<br />
packages&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackagesBulk.zip">CL181</a> (KindOfPackagesBulk)<br />
THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping marks&gt; =<br />
"O"<br />
AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br />
packages&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of<br />
packages&gt; is in SET <a href="../downloads/CL182.zip">CL182</a> (KindOfPackagesUnpacked)<br />
THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping marks&gt; =<br />
"O"<br />
AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br />
packages&gt; = "R"<br />
ELSE<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping marks&gt; =<br />
"R"<br />
AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br />
packages&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackagesBulk.zip">CL181</a><br />
THEN<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks = "O" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages is in SET<br />
<a href="../downloads/CL182.zip">CL182</a><br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks = "O"<br />
AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks ="R"<br />
AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages = "R"


## C0085

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeWithReference.zip">CL076</a> (GuaranteeTypeWithReference)<br />
THEN &lt;GUARANTEE.GUARANTEE REFERENCE&gt; = "R"<br />
ELSE &lt;GUARANTEE.GUARANTEE REFERENCE&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeWithReference.zip">CL076</a><br />
THEN /<span>&#42;</span>/Guarantee/GuaranteeReference = "R"<br />
ELSE /<span>&#42;</span>/Guarantee/GuaranteeReference = "N"


## C0086

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeWithGRN.zip">CL286</a> (GuaranteeTypeWithGRN)<br />
THEN<br />
&lt;GUARANTEE.GUARANTEE REFERENCE.GRN&gt; = "R" AND<br />
&lt;GUARANTEE.GUARANTEE REFERENCE.Access code&gt; = "R"<br />
ELSE<br />
&lt;GUARANTEE.GUARANTEE REFERENCE.GRN&gt; = "N" AND<br />
&lt;GUARANTEE.GUARANTEE REFERENCE.Access code&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeWithGRN.zip">CL286</a><br />
THEN /<span>&#42;</span>/Guarantee/GuaranteeReference/GRN = "R" AND<br />
/<span>&#42;</span>/Guarantee/GuaranteeReference/accessCode = "R"<br />
ELSE /<span>&#42;</span>/Guarantee/GuaranteeReference/GRN = "N" AND<br />
/<span>&#42;</span>/Guarantee/GuaranteeReference/accessCode = "N"


## C0101

**Functional Description**

IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br />
THEN &lt;AUTHORISATION&gt; = "R"<br />
ELSE &lt;AUTHORISATION&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator is EQUAL to '1'<br />
THEN /<span>&#42;</span>/Authorisation = "R"<br />
ELSE /<span>&#42;</span>/Authorisation = "O"


## C0102

**Functional Description**

IF &lt;TRANSIT OPERATION.Simplified procedure&gt; is EQUAL to '1'<br />
THEN &lt;CC007C-AUTHORISATION&gt; = "R"<br />
ELSE &lt;CC007C-AUTHORISATION&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/simplifiedProcedure is EQUAL to '1'<br />
THEN /CC007C/Authorisation = "R"<br />
ELSE /CC007C/Authorisation = "N"


## C0128

**Functional Description**

IF the first three characters of &lt;Message recipient&gt; is EQUAL to ‘NTA’<br />
THEN &lt;INVALIDATION.Decision&gt; = "N"<br />
ELSE &lt;INVALIDATION.Decision&gt; = "R"

**Technical Description**

IF the first three characters of /<span>&#42;</span>/messageRecipient is EQUAL to ‘NTA’<br />
THEN /<span>&#42;</span>/Invalidation/decision = "N"<br />
ELSE /<span>&#42;</span>/Invalidation/decision = "R"


## C0129

**Functional Description**

IF &lt;INVALIDATION.Initiated by customs&gt; is EQUAL to ‘1’<br />
THEN &lt;INVALIDATION.Request date and time&gt; = "N"<br />
ELSE &lt;INVALIDATION.Request date and time&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/Invalidation/initiatedByCustoms is EQUAL to ‘1’<br />
THEN /<span>&#42;</span>/Invalidation/requestDateAndTime = "N"<br />
ELSE /<span>&#42;</span>/Invalidation/requestDateAndTime = "R"


## C0130

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is EQUAL to '8'<br />
THEN &lt;GUARANTEE.Other guarantee reference&gt; = "R"<br />
ELSE IF &lt;GUARANTEE.Guarantee type&gt; is EQUAL to '3'<br />
THEN &lt;GUARANTEE.Other guarantee reference&gt; = "O"<br />
ELSE &lt;GUARANTEE.Other guarantee reference&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to '8'<br />
THEN /<span>&#42;</span>/Guarantee/otherGuaranteeReference = "R"<br />
ELSE IF /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to '3'<br />
THEN /<span>&#42;</span>/Guarantee/otherGuaranteeReference = "O"<br />
ELSE /<span>&#42;</span>/Guarantee/otherGuaranteeReference = "N"


## C0137

**Functional Description**

IF the first three characters of &lt;Message recipient&gt; is EQUAL to ‘NTA’<br />
THEN &lt;INVALIDATION.Justification&gt; = "R"<br />
ELSE &lt;INVALIDATION.Justification&gt; = "O"

**Technical Description**

IF the first three characters of /<span>&#42;</span>/messageRecipient is EQUAL to ‘NTA’<br />
THEN /<span>&#42;</span>/Invalidation/justification = "R"<br />
ELSE /<span>&#42;</span>/Invalidation/justification = "O"


## C0153

**Functional Description**

IF &lt;TRANSIT OPERATION.DeclarationType&gt; is EQUAL to ‘TIR’ AND &lt;CONSIGNMENT-HOUSE<br />
CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; IS NOT EQUAL to ‘N830’ (Goods declaration for<br />
exportation)<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br />
COMMODITY CODE&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br />
COMMODITY CODE&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to ‘TIR’ AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/type IS NOT EQUAL to ‘N830’ (Goods<br />
declaration for exportation)<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode = "R"


## C0170

**Functional Description**

IF &lt;CC015C-TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br />
  OR &lt;CC013C-TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br />
THEN &lt;CC170C-CONSIGNMENT.Inland mode of transport&gt; = "N"<br />
ELSE &lt;CC170C-CONSIGNMENT.Inland mode of transport&gt; = "O"

**Technical Description**

IF /CC015C/TransitOperation/reducedDatasetIndicator is EQUAL to '1'<br />
  OR /CC013C/TransitOperation/reducedDatasetIndicator is EQUAL to '1'<br />
THEN /CC170C/Consignment/inlandModeOfTransport = "N"<br />
ELSE /CC170C/Consignment/inlandModeOfTransport = "O"


## C0186

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to ’0'<br />
THEN<br />
&lt;CONSIGNMENT-TRANSPORT CHARGES&gt; = "N" AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt; = "N"<br />
ELSE<br />
&lt;CONSIGNMENT-TRANSPORT CHARGES&gt; = "O" AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '0'<br />
THEN /<span>&#42;</span>/Consignment/TransportCharges = "N"<br />
AND /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges = "N"<br />
ELSE /<span>&#42;</span>/Consignment/TransportCharges = "O"<br />
AND /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges = "O"


## C0190

**Functional Description**

IF &lt;CC015C-TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br />
THEN &lt;CC190C-TRANSIT OPERATION.TIR carnet number&gt; = "R"<br />
ELSE &lt;CC190C-TRANSIT OPERATION.TIR carnet number&gt; = "N"

**Technical Description**

IF /CC015C/TransitOperation/declarationType is EQUAL to 'TIR'<br />
THEN /CC190C/TransitOperation/TIRCarnetNumber = "R"<br />
ELSE /CC190C/TransitOperation/TIRCarnetNumber = "N"


## C0191

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 3}<br />
THEN<br />
&lt;CONSIGNMENT-PLACE OF UNLOADING&gt; = "R"<br />
ELSE<br />
IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to ‘0’<br />
THEN<br />
&lt;CONSIGNMENT-PLACE OF UNLOADING&gt; = "N"<br />
ELSE<br />
&lt;CONSIGNMENT-PLACE OF UNLOADING&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 3}<br />
THEN<br />
/<span>&#42;</span>/Consignment/PlaceOfUnloading = "R"<br />
ELSE<br />
IF /<span>&#42;</span>/TransitOperation/security is EQUAL to ‘0’<br />
THEN<br />
/<span>&#42;</span>/Consignment/PlaceOfUnloading = "N"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/PlaceOfUnloading = "O"


## C0215

**Functional Description**

IF &lt;CC141C-ENQUIRY.Text&gt; is PRESENT<br />
   THEN<br />
 IF &lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; is PRESENT<br />
 THEN &lt;CC141C-CONSIGNMENT&gt; = "O"<br />
 ELSE &lt;CC141C-CONSIGNMENT&gt; = "R"<br />
ELSE &lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; = "N"<br />
AND &lt;CC141C-CONSIGNMENT&gt; = "N"

**Technical Description**

IF /CC141C/Enquiry/text is PRESENT<br />
THEN<br />
   IF /CC141C/CustomsOfficeOfDestinationActual is PRESENT<br />
   THEN /CC141C/Consignment = "O"<br />
ELSE /CC141C/Consignment = "R"<br />
ELSE /CC141C/CustomsOfficeOfDestinationActual = "N"<br />
AND /CC141C/Consignment = "N"


## C0220

**Functional Description**

IF &lt;CC141C-ENQUIRY.TC11 delivery date&gt; is PRESENT<br />
THEN &lt;CC141C-ENQUIRY.Text&gt; = "R"<br />
ELSE &lt;CC141C-ENQUIRY.Text&gt; = "O"

**Technical Description**

IF /CC141C/Enquiry/TC11DeliveryDate is PRESENT<br />
THEN /CC141C/Enquiry/text = "R"<br />
ELSE /CC141C/Enquiry/text = "O"


## C0231

**Functional Description**

IF &lt;CC037C-GUARANTEE REFERENCE.Guarantee type&gt; is in SET {0, 1}<br />
THEN<br />
&lt;CC037C-GUARANTEE REFERENCE-USAGE.Arrival date and time&gt; = "R" AND<br />
&lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE.Reference amount = "R"<br />
AND<br />
&lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE.Percentage of reference<br />
amount&gt; = "R"<br />
ELSE<br />
&lt;CC037C-GUARANTEE REFERENCE-USAGE.Arrival date and time&gt; = "N" AND<br />
&lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE.Reference amount = "N"<br />
AND<br />
&lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE.Percentage of reference<br />
amount&gt; = "N"

**Technical Description**

IF /CC037C/GuaranteeReference/guaranteeType is in SET {0, 1}<br />
THEN /CC037C/GuaranteeReference/Usage/arrivalDateAndTime = "R"<br />
AND /CC037C/GuaranteeReference/ComprehensiveGuarantee/referenceAmount = "R"<br />
AND /CC037C/GuaranteeReference/ComprehensiveGuarantee/percentageOfReferenceAmount = "R"<br />
ELSE /CC037C/GuaranteeReference/Usage/arrivalDateAndTime = "N"<br />
AND /CC037C/GuaranteeReference/ComprehensiveGuarantee/referenceAmount = "N"<br />
AND /CC037C/GuaranteeReference/ComprehensiveGuarantee/percentageOfReferenceAmount ="N"


## C0232

**Functional Description**

IF &lt;GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER.TIR Carnet&gt; is EQUAL to ’1’<br />
THEN &lt;GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER.Voucher amount&gt; = "R"<br />
AND &lt;GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER.Currency&gt; = "R"<br />
ELSE &lt;GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER.Voucher amount&gt; = "N"<br />
AND &lt;GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER.Currency&gt; = "N";<br />
IF &lt;GUARANTEE REFERENCE.TIR Carnet&gt; is EQUAL to ’1’<br />
THEN &lt;GUARANTEE REFERENCE.Voucher amount&gt; = "R"<br />
AND &lt;GUARANTEE REFERENCE.Currency&gt; = "R"<br />
ELSE &lt;GUARANTEE REFERENCE.Voucher amount&gt; = "N"<br />
AND &lt;GUARANTEE REFERENCE.Currency&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/GuaranteeReference/IndividualGuaranteeVoucher/TIRCarnet is EQUAL to ’1’<br />
THEN /<span>&#42;</span>/GuaranteeReference/IndividualGuaranteeVoucher/voucherAmount= "R"<br />
AND /<span>&#42;</span>/GuaranteeReference/IndividualGuaranteeVoucher/currency = "R"<br />
ELSE /<span>&#42;</span>/GuaranteeReference/IndividualGuaranteeVoucher/voucherAmount = "N"<br />
AND /<span>&#42;</span>/GuaranteeReference/IndividualGuaranteeVoucher/currency = "N";<br />
IF /<span>&#42;</span>/GuaranteeReference/TIRCarnet is EQUAL to ’1’<br />
THEN /<span>&#42;</span>/GuaranteeReference/voucherAmount= "R"<br />
AND /<span>&#42;</span>/GuaranteeReference/currency = "R"<br />
ELSE /<span>&#42;</span>/GuaranteeReference/voucherAmount = "N"<br />
AND /<span>&#42;</span>/GuaranteeReference/currency = "N"


## C0233

**Functional Description**

IF at least one occurrence of &lt;GUARANTEE.Guarantee type&gt; is EQUAL to ‘2’<br />
THEN &lt;CUSTOMS OFFICE OF DESTINATION (DECLARED)&gt; = "R"<br />
ELSE &lt;CUSTOMS OFFICE OF DESTINATION (DECLARED)&gt; = "N"

**Technical Description**

IF at least one occurrence of /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to ‘2’<br />
THEN /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared = "R"<br />
ELSE /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared = "N"


## C0234

**Functional Description**

IF &lt;CC037C-GUARANTEE REFERENCE.Guarantee type&gt; is in SET {1, 2, 4, 9}<br />
THEN &lt;CC037C-GUARANTEE REFERENCE-GUARANTOR&gt; ="R"<br />
ELSE &lt;CC037C-GUARANTEE REFERENCE-GUARANTOR&gt; = "N"

**Technical Description**

IF /CC037C/GuaranteeReference/guaranteeType is in SET {1, 2, 4, 9}<br />
THEN /CC037C/GuaranteeReference/Guarantor = "R"<br />
ELSE /CC037C/GuaranteeReference/Guarantor = "N"


## C0240

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT.Code&gt; is in SET {2, 4}<br />
THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt; = "R" AND<br />
&lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-INCIDENT.Code&gt; is in SET {3, 6}<br />
THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt; = "O" AND<br />
&lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT&gt; = "R"<br />
ELSE<br />
&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt; = "N" AND<br />
&lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/code is in SET {2, 4}<br />
THEN /<span>&#42;</span>/Consignment/Incident/TransportEquipment = "R" AND<br />
/<span>&#42;</span>/Consignment/Incident/Transhipment = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/Incident/code is in SET {3, 6}<br />
THEN /<span>&#42;</span>/Consignment/Incident/TransportEquipment = "O" AND<br />
/<span>&#42;</span>/Consignment/Incident/Transhipment = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment = "N" AND<br />
/<span>&#42;</span>/ Consignment/Incident/Transhipment = "N"


## C0250

**Functional Description**

IF &lt;HOLDER OF THE TRANSIT PROCEDURE.Identification number&gt; is PRESENT<br />
AND &lt;HOLDER OF THE TRANSIT PROCEDURE.Identification number&gt; is a valid identifier in the<br />
European EOS ((Economic Operators Systems) verified by the EU Member State receiving or sending<br />
this message), OR is a valid identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
 &lt;HOLDER OF THE TRANSIT PROCEDURE.Name&gt; = "N" AND<br />
&lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS&gt; = "N"<br />
ELSE<br />
 &lt;HOLDER OF THE TRANSIT PROCEDURE.Name&gt; = "R" AND<br />
 &lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS&gt; = "R";<br />
IF &lt;CONSIGNMENT-CONSIGNOR.Identification number&gt; is PRESENT<br />
AND &lt;CONSIGNMENT-CONSIGNOR.Identification number&gt; is a valid identifier in the European EOS<br />
((Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br />
OR is a valid identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
   &lt;CONSIGNMENT-CONSIGNOR.Name&gt; = "N" AND<br />
   &lt;CONSIGNMENT-CONSIGNOR-ADDRESS&gt; = "N"<br />
ELSE<br />
  &lt;CONSIGNMENT-CONSIGNOR.Name&gt; = "R" AND<br />
 &lt;CONSIGNMENT-CONSIGNOR-ADDRESS&gt; = "R";<br />
IF &lt;CONSIGNMENT-CONSIGNEE.Identification number&gt; is PRESENT<br />
AND &lt;CONSIGNMENT-CONSIGNEE.Identification number&gt; is a valid identifier in the European EOS<br />
((Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br />
OR is a valid identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
  &lt;CONSIGNMENT-CONSIGNEE.Name&gt; = "N" AND<br />
  &lt;CONSIGNMENT-CONSIGNEE-ADDRESS&gt; = "N"<br />
ELSE<br />
  &lt;CONSIGNMENT-CONSIGNEE.Name&gt; = "R" AND<br />
  &lt;CONSIGNMENT-CONSIGNEE-ADDRESS&gt; = "R";<br />
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Identification number&gt; is PRESENT<br />
AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Identification number is a valid<br />
identifier in the European EOS ((Economic Operators Systems) verified by the EU Member State<br />
receiving or sending this message), OR is a valid identifier in the DB of the CTC country receiving or<br />
sending this message<br />
THEN<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Name&gt; = "N" AND<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS&gt; = "N"<br />
ELSE<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Name&gt; = "R" AND<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS&gt; = "R";<br />
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Identification number&gt; is PRESENT<br />
AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Identification number&gt;<br />
is a valid identifier in the European EOS ((Economic Operators Systems) verified by the EU Member<br />
State receiving or sending this message), OR is a valid identifier in the DB of the CTC country<br />
receiving or sending this message<br />
THEN<br />
   &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Name&gt; = "N" AND<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS&gt; = "N"<br />
ELSE<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Name&gt; = "R" AND<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS&gt; = "R";<br />
IF &lt;GUARANTOR.Identification number&gt; is PRESENT AND &lt;GUARANTOR.Identification number&gt;<br />
is a valid identifier in the European EOS ((Economic Operators Systems) verified by the EU Member<br />
State receiving or sending this message), OR is a valid identifier in the DB of the CTC country<br />
receiving or sending this message<br />
THEN<br />
 &lt;GUARANTOR.Name&gt; = "N" AND<br />
 &lt;GUARANTOR-ADDRESS&gt; = "N"<br />
ELSE<br />
 &lt;GUARANTOR.Name&gt; = "R" AND<br />
&lt;GUARANTOR-ADDRESS&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/HolderOfTheTransitProcedure/identificationNumber is PRESENT AND<br />
/<span>&#42;</span>/HolderOfTheTransitProcedure/identificationNumber is a valid identifier in the European EOS<br />
((Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br />
OR is a valid identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
 /<span>&#42;</span>/HolderOfTheTransitProcedure/name="N" AND<br />
 /<span>&#42;</span>/HolderOfTheTransitProcedure/Address="N"<br />
ELSE<br />
  /<span>&#42;</span>/HolderOfTheTransitProcedure/name="R" AND<br />
  /<span>&#42;</span>/HolderOfTheTransitProcedure/Address="R";<br />
IF /<span>&#42;</span>/Consignment/Consignor/identificationNumber is PRESENT AND<br />
/<span>&#42;</span>/Consignment/Consignor/identificationNumber is a valid identifier in in the European EOS ((Economic<br />
Operators Systems) verified by the EU Member State receiving or sending this message), OR is a valid<br />
identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
 /<span>&#42;</span>/Consignment/Consignor/name="N" AND<br />
/<span>&#42;</span>/Consignment/Consignor/Address="N"<br />
ELSE<br />
   /<span>&#42;</span>/Consignment/Consignor/name="R" AND<br />
  /<span>&#42;</span>/Consignment/Consignor/Address="R";<br />
IF /<span>&#42;</span>/Consignment/Consignee/identificationNumber is PRESENT<br />
AND /<span>&#42;</span>/Consignment/Consignee/identificationNumber is a valid identifier in the European EOS<br />
(Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br />
OR is a valid identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
   /<span>&#42;</span>/Consignment/Consignee/name="N" AND<br />
   /<span>&#42;</span>/Consignment/Consignee/Address="N"<br />
ELSE<br />
  /<span>&#42;</span>/Consignment/Consignee/name="R" AND<br />
 /<span>&#42;</span>/Consignment/Consignee/Address="R";<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/identificationNumber is PRESENT<br />
AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/identificationNumber is a valid identifier in the<br />
European EOS ((Economic Operators Systems) verified by the EU Member State receiving or sending<br />
this message), OR is a valid identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/name="N" AND<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address="N"<br />
ELSE<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/name="R" AND<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address="R";<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/identificationNumber is PRESENT<br />
AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/identificationNumber is a valid identifier in the<br />
European EOS ((Economic Operators Systems) verified by the EU Member State receiving or sending<br />
this message), OR is a valid identifier in the DB of the CTC country receiving or sending this message<br />
THEN<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/name="N" AND<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address="N"<br />
ELSE<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/name="R" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address="R";<br />
IF /<span>&#42;</span>/Guarantor/identificationNumber is PRESENT AND<br />
/<span>&#42;</span>/Guarantor/identificationNumber is a valid identifier in the European EOS ((Economic Operators<br />
Systems) verified by the EU Member State receiving or sending this message), OR is a valid identifier<br />
in the DB of the CTC country receiving or sending this message<br />
THEN<br />
  /<span>&#42;</span>/Guarantor/name="N" AND<br />
 /<span>&#42;</span>/Guarantor/Address="N"<br />
ELSE<br />
 /<span>&#42;</span>/Guarantor/name="R" AND<br />
/<span>&#42;</span>/Guarantor/Address="R";


## C0251

**Functional Description**

IF &lt;RISK ANALYSIS IDENTIFICATION.Code&gt; is in SET {R,Y}<br />
THEN &lt;RISK ANALYSIS IDENTIFICATION–RISK ANALYSIS&gt; = "R"<br />
ELSE<br />
 IF &lt;RISK ANALYSIS IDENTIFICATION.Code&gt; is EQUAL to 'X'<br />
THEN<br />
   IF the last two characters of &lt;Message sender&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
(CountryCodesCommunity)<br />
   THEN &lt;RISK ANALYSIS IDENTIFICATION–RISK ANALYSIS&gt; = "R"<br />
   ELSE &lt;RISK ANALYSIS IDENTIFICATION–RISK ANALYSIS&gt; = "O"<br />
 ELSE &lt;RISK ANALYSIS IDENTIFICATION–RISK ANALYSIS&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/RiskAnalysisIdentification/code is in SET {R, Y}<br />
THEN /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis = "R"<br />
ELSE<br />
 IF /<span>&#42;</span>/RiskAnalysisIdentification/code is EQUAL to ‘X’<br />
 THEN<br />
  IF the last two characters of /<span>&#42;</span>/messageSender is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
  THEN /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis = "R"<br />
   ELSE /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis = "O"<br />
 ELSE /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis = "N"


## C0255

**Functional Description**

IF &lt;CD204C-TRANSIT OPERATION.Usage cancellation date&gt; is PRESENT<br />
THEN &lt;CD204C-TRANSIT OPERATION.Release date&gt; = "N"<br />
ELSE &lt;CD204C-TRANSIT OPERATION.Release date&gt; = "R"

**Technical Description**

IF /CD204C/TransitOperation/usageCancellationDate is PRESENT<br />
THEN /CD204C/TransitOperation/releaseDate = "N"<br />
ELSE /CD204C/TransitOperation/releaseDate = "R"


## C0260

**Functional Description**

IF &lt;CC225C-GUARANTEE REFERENCE.Validity date&gt; is PRESENT<br />
THEN &lt;CC225C-GUARANTEE REFERENCE.Invalidity date&gt; = "N"<br />
ELSE &lt;CC225C-GUARANTEE REFERENCE.Invalidity date&gt; = "O"

**Technical Description**

IF /CC225C/GuaranteeReference/validityDate is PRESENT<br />
THEN /CC225C/GuaranteeReference/invalidityDate&gt; = "N"<br />
ELSE /CC225C/GuaranteeReference/invalidityDate&gt; = "O"


## C0270

**Functional Description**

IF &lt;CC037C-GUARANTEE REFERENCE-GUARANTEE QUERY.Query identifier&gt; is EQUAL to ‘4’<br />
THEN &lt;CC037C-GUARANTEE REFERENCE.Owner&gt; = "R"<br />
ELSE &lt;CC037C-GUARANTEE REFERENCE.Owner&gt; = "N"

**Technical Description**

IF /CC037C/GuaranteeReference/GuaranteeQuery/queryIdentifier is EQUAL to ‘4’<br />
THEN /CC037C/GuaranteeReference/Owner = "R"<br />
ELSE /CC037C/GuaranteeReference/Owner = "N"


## C0280

**Functional Description**

IF &lt;CC037C-GUARANTEE REFERENCE-GUARANTEE QUERY.Query identifier&gt; is EQUAL to ‘4’<br />
THEN &lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE&gt; = "N" AND<br />
&lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE BY GUARANTOR&gt; = "N" AND<br />
&lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER&gt; = "N"<br />
ELSE IF &lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE&gt; is PRESENT<br />
THEN &lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE BY GUARANTOR&gt; = "N"<br />
AND<br />
&lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER&gt; = "N"<br />
ELSE IF &lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE BY GUARANTOR&gt; is<br />
PRESENT<br />
THEN &lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE&gt; = "N" AND<br />
&lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER&gt; = "N"<br />
ELSE &lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE VOUCHER&gt; = "R" AND<br />
&lt;CC037C-GUARANTEE REFERENCE-COMPREHENSIVE GUARANTEE&gt; = "N" AND<br />
&lt;CC037C-GUARANTEE REFERENCE-INDIVIDUAL GUARANTEE BY GUARANTOR&gt; = "N"

**Technical Description**

IF /CC037C/GuaranteeReference/GuaranteeQuery/queryIdentifier is EQUAL to ‘4’<br />
THEN /CC037C/GuaranteeReference/ComprehensiveGuarantee = "N" AND<br />
/CC037C/GuaranteeReference/IndividualGuaranteeByGuarantor = "N" AND<br />
/CC037C/GuaranteeReference/IndividualGuaranteeVoucher = "N"<br />
ELSE IF /CC037C/GuaranteeReference/ComprehensiveGuarantee is PRESENT<br />
THEN /CC037C/GuaranteeReference/IndividualGuaranteeByGuarantor = "N" AND<br />
/CC037C/GuaranteeReference/IndividualGuaranteeVoucher = "N"<br />
ELSE IF /CC037C/GuaranteeReference/IndividualGuaranteeByGuarantor is PRESENT<br />
THEN /CC037C/GuaranteeReference/ComprehensiveGuarantee = "N" AND<br />
/CC037C/GuaranteeReference/IndividualGuaranteeVoucher = "N"<br />
ELSE /CC037C/GuaranteeReference/IndividualGuaranteeVoucher = "R" AND<br />
/CC037C/GuaranteeReference/ComprehensiveGuarantee = "N" AND<br />
/CC037C/GuaranteeReference/IndividualGuaranteeByGuarantor = "N"


## C0285

**Functional Description**

IF &lt;CC037C-GUARANTEE REFERENCE-GUARANTEE QUERY.Query identifier&gt; is in SET {1,4}<br />
OR &lt;CC037C-GUARANTEE REFERENCE.Guarantee type&gt; is EQUAL to '4'<br />
THEN &lt;CC037C-GUARANTEE REFERENCE-EXPOSURE&gt; = "N"<br />
ELSE &lt;CC037C-GUARANTEE REFERENCE-EXPOSURE&gt; = "R"

**Technical Description**

IF /CC037C/GuaranteeReference/GuaranteeQuery/queryIdentifier is in SET {1,4}<br />
OR /CC037C/GuaranteeReference/guaranteeType is EQUAL to '4'<br />
THEN /CC037C/GuaranteeReference/Exposure = "N"<br />
ELSE /CC037C/GuaranteeReference/Exposure = "R"


## C0286

**Functional Description**

IF &lt;CC037C-GUARANTEE REFERENCE.Guarantee monitoring code&gt; is EQUAL to ‘3’<br />
THEN &lt;CC037C-GUARANTEE REFERENCE-EXPOSURE.Balance&gt; = "R"<br />
ELSE &lt;CC037C-GUARANTEE REFERENCE-EXPOSURE.Balance&gt; = "N"

**Technical Description**

IF /CC037C/GuaranteeReference/guaranteeMonitoringCode is EQUAL to ‘3’<br />
THEN /CC037C/GuaranteeReference/Exposure/balance = "R"<br />
ELSE /CC037C/GuaranteeReference/Exposure/balance = "N"


## C0298

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br />
DOCUMENT.Quantity&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br />
DOCUMENT.Measurement unit and qualifier&gt; = "R"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br />
DOCUMENT.Measurement unit and qualifier&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/quantity&gt; is PRESENT<br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/measurementUnitAndQualifi<br />
er = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/measurementUnitAndQualifi<br />
er = "N"


## C0315

**Functional Description**

IF &lt;CC141C-ENQUIRY.TC11 delivery date&gt; is PRESENT<br />
THEN &lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; = "R"<br />
ELSE &lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; = "O"

**Technical Description**

IF /CC141C/ENQUIRY/TC11DeliveryDate is PRESENT<br />
THEN /CC141C/CustomsOfficeOfDestinationActual = "R"<br />
ELSE /CC141C/CustomsOfficeOfDestinationActual= "O"


## C0320

**Functional Description**

IF &lt;CD144C-RESPONSE INFORMATION.Information Code&gt; is in SET {10, 40, 50}<br />
THEN &lt;CD144C-RESPONSE INFORMATION.Text&gt; = "R"<br />
ELSE &lt;CD144C-RESPONSE INFORMATION.Text&gt; = "N"

**Technical Description**

IF /CD144C/ResponseInformation/informationCode&gt; is in SET {10, 40, 50}<br />
THEN /CD144C/ResponseInformation/text = "R"<br />
ELSE /CD144C/ResponseInformation/text = "N"


## C0330

**Functional Description**

IF &lt;CD145C-REQUESTED INFORMATION.Code&gt; is in SET {5, 6}<br />
THEN &lt;CD145C-REQUESTED INFORMATION.Text&gt; = "R"<br />
ELSE &lt;CD145C-REQUESTED INFORMATION.Text&gt; = "N"

**Technical Description**

IF /CD145C/RequestedInformation/code is in SET {5, 6}<br />
THEN /CD145C/RequestedInformation/text = "R"<br />
ELSE /CD145C/RequestedInformation/text = "N"


## C0333

**Functional Description**

IF &lt;CC029C-CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = “R”<br />
 ELSE&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = “N”;<br />
IF &lt;CC029C-CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is<br />
PRESENT<br />
THEN<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = “R”<br />
ELSE<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = “N”

**Technical Description**

IF /CC029C/Consignment/DepartureTransportMeans is PRESENT<br />
THEN<br />
   /<span>&#42;</span>/ Consignment/DepartureTransportMeans = “R”<br />
ELSE<br />
  /<span>&#42;</span>/ Consignment/DepartureTransportMeans = “N”;<br />
IF /CC029C/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT<br />
THEN<br />
   /<span>&#42;</span>/ Consignment/HouseConsignment/DepartureTransportMeans = “R”<br />
ELSE<br />
 /<span>&#42;</span>/ Consignment/HouseConsignment/DepartureTransportMeans = “N”


## C0337

**Functional Description**

IF &lt;CONSIGNMENT-TRANSPORT CHARGES&gt; is PRESENT<br />
THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt; = "N"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt;<br />
= "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/TransportCharges is PRESENT<br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges = "O"


## C0339

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '5'<br />
THEN<br />
&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "N" AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "N"<br />
ELSE<br />
IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "N"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '5'<br />
THEN<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans = “N” AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans = "N"<br />
ELSE<br />
IF/<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans = "O"


## C0343

**Functional Description**

IF &lt;CONSIGNMENT.Country of destination&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination&gt; =<br />
"N"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination&gt; =<br />
"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination = "R"


## C0349
  
  **Functional Description**
  
  IF &lt;CONSIGNMENT-CONSIGNOR&gt; is PRESENT<br />
THEN<br />
   &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; = "N"<br />
ELSE<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; = "O"
  
  **Technical Description**
  
  IF /<span>&#42;</span>/Consignment/Consignor is PRESENT<br />
 THEN<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/Consignor = "N"<br />
 ELSE<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/Consignor = "O"
  

## C0352

**Functional Description**

IF &lt;TRANSIT OPERATION.Release indicator&gt; is in SET {2,3}<br />
THEN &lt;CONSIGNMENT&gt; = ''R''<br />
ELSE &lt;CONSIGNMENT&gt; = ''N''

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/releaseIndicator is in SET {2,3}<br />
THEN /<span>&#42;</span>/Consignment = ''R''<br />
ELSE /<span>&#42;</span>/Consignment = ''N''


## C0353

**Functional Description**

IF &lt;CONSIGNMENT.HOUSE CONSIGNMENT.Release type &gt; is EQUAL to '1'<br />
THEN &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT ITEM&gt; = ''R''<br />
ELSE &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT ITEM&gt; = ''N''

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/releaseType is EQUAL to '1'<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem = ''R''<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem = ''N''


## C0354

**Functional Description**

IF &lt;CD049C-TRANSIT OPERATION.Discrepancies resolved&gt; is EQUAL to ‘1’<br />
THEN &lt;CD049C-TRANSIT OPERATION.Write-off date&gt; = ''R''<br />
ELSE &lt;CD049C-TRANSIT OPERATION.Write-off date&gt; = ''N''

**Technical Description**

IF /CD049C/TransitOperation/discrepanciesResolved is EQUAL to ‘1’<br />
THEN /CD049C/TransitOperation/writeOffDate = ''R''<br />
ELSE /CD049C/TransitOperation/writeOffDate = ''N''


## C0365

**Functional Description**

IF&lt;TRANSIT OPERATION. Request Rejection Reason Code&gt; is PRESENT<br />
THEN<br />
&lt;TRANSIT OPERATION.Declaration type&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.Declaration acceptance date&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.Release date&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.Reduced dataset indicator&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.Binding itinerary&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.Security&gt; = "N" AND<br />
&lt;CUSTOMS OFFICE OF DESTINATION (DECLARED)&gt; = "N" AND<br />
&lt;CONTROL RESULT&gt; = "N" AND<br />
&lt;HOLDER OF THE TRANSIT PROCEDURE&gt; = "N" AND<br />
&lt;CONSIGNMENT&gt; = "N" AND<br />
&lt;CD038C/TRANSIT OPERATION.Status&gt; = "N"<br />
ELSE<br />
&lt;TRANSIT OPERATION.Declaration type&gt; = "R" AND<br />
&lt;TRANSIT OPERATION.Declaration acceptance date&gt; = "R" AND<br />
&lt;TRANSIT OPERATION.Release date&gt; = "R" AND<br />
&lt;TRANSIT OPERATION.Reduced dataset indicator&gt; = "R" AND<br />
&lt;TRANSIT OPERATION.Binding itinerary&gt; = "R" AND<br />
&lt;TRANSIT OPERATION.Security&gt; = "R" AND<br />
&lt;CUSTOMS OFFICE OF DESTINATION (DECLARED)&gt; = "R" AND<br />
&lt;CONTROL RESULT&gt; = "R" AND<br />
&lt;HOLDER OF THE TRANSIT PROCEDURE&gt; = "R" AND<br />
&lt;CONSIGNMENT&gt; = "R" AND<br />
&lt;CD038C/TRANSIT OPERATION.Status&gt; = "R"

**Technical Description**

IF/<span>&#42;</span>/TransitOperation/requestRejectionReasonCode is PRESENT<br />
THEN /<span>&#42;</span>/TransitOperation/declarationType = "N"<br />
AND /<span>&#42;</span>/TransitOperation/declarationAcceptanceDate = "N"<br />
AND /<span>&#42;</span>/TransitOperation/releaseDate = "N"<br />
AND /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator = "N"<br />
AND /<span>&#42;</span>/TransitOperation/bindingItinerary = "N"<br />
AND /<span>&#42;</span>/TransitOperation/security = "N"<br />
AND /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared = "N"<br />
AND /<span>&#42;</span>/ControlResult = "N"<br />
AND /<span>&#42;</span>/HolderOfTheTransitProcedure = "N"<br />
AND /<span>&#42;</span>/Consignment = "N"<br />
AND /CD038C/TransitOperation/status = "N"<br />
ELSE /<span>&#42;</span>/TransitOperation/declarationType = "R"<br />
AND /<span>&#42;</span>/TransitOperation/declarationAcceptanceDate = "R"<br />
AND /<span>&#42;</span>/TransitOperation/releaseDate = "R"<br />
AND /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator = "R"<br />
AND /<span>&#42;</span>/TransitOperation/bindingItinerary = "R"<br />
AND /<span>&#42;</span>/TransitOperation/security = "R"<br />
AND /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared = "R"<br />
AND /<span>&#42;</span>/ControlResult = "R"<br />
AND /<span>&#42;</span>/HolderOfTheTransitProcedure = "R"<br />
AND /<span>&#42;</span>/Consignment = "R"<br />
AND /CD038C/TransitOperation/status = "R"


## C0366

**Functional Description**

IF&lt;CD165C-TRANSIT OPERATION.Request rejection reason code&gt; is PRESENT<br />
THEN &lt;CD165C-TRANSIT OPERATION.Specific circumstance indicator&gt; = "N" AND<br />
&lt;CD165C-CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "N" AND no validation of other<br />
conditions is performed<br />
ELSE &lt;CD165C-TRANSIT OPERATION.Specific circumstance indicator&gt; = "O" AND<br />
&lt;CD165C-CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "O"

**Technical Description**

IF /CD165C/TransitOperation/requestRejectionReasonCode is PRESENT<br />
THEN /CD165C/TransitOperation/specificCircumstanceIndicator = "N" AND<br />
/CD165C/CustomsOfficeOfTransitDeclared = "N"<br />
AND no validation of other conditions is performed<br />
ELSE /CD165C/TransitOperation/specificCircumstanceIndicator = "O" AND<br />
/CD165C/CustomsOfficeOfTransitDeclared = "O"


## C0382

**Functional Description**

IF &lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryAddressPostcodeOnly.zip">CL198</a><br />
THEN &lt;CONSIGNMENT-LOCATION OF GOODS- POSTCODE ADDRESS. House number&gt; = ''O''<br />
ELSE &lt;CONSIGNMENT-LOCATION OF GOODS- POSTCODE ADDRESS.House number&gt; = ''R''

**Technical Description**

IF /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryAddressPostcodeOnly.zip">CL198</a><br />
THEN /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress/houseNumber = ''O''<br />
ELSE /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress/houseNumber = ''R''


## C0387

**Functional Description**

IF &lt;CONSIGNMENT-PLACE OF LOADING.UN LOCODE&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-PLACE OF LOADING.Country&gt; = "O" AND<br />
&lt;CONSIGNMENT-PLACE OF LOADING.Location&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-PLACE OF LOADING.Country&gt; = "R" AND<br />
&lt;CONSIGNMENT-PLACE OF LOADING.Location&gt; = "R";<br />
IF &lt;CONSIGNMENT-PLACE OF UNLOADING.UN LOCODE&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-PLACE OF UNLOADING.Country&gt; = "O" AND<br />
&lt;CONSIGNMENT-PLACE OF UNLOADING.Location&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-PLACE OF UNLOADING.Country&gt; = "R" AND<br />
&lt;CONSIGNMENT-PLACE OF UNLOADING.Location&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/PlaceOfLoading/UNLocode is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/PlaceOfLoading/country = "O" AND<br />
/<span>&#42;</span>/Consignment/PlaceOfLoading/location = "O"<br />
ELSE /<span>&#42;</span>/Consignment/PlaceOfLoading/country = "R" AND<br />
/<span>&#42;</span>/Consignment/PlaceOfLoading/location = "R";<br />
IF /<span>&#42;</span>/Consignment/PlaceOfUnloading/UNLocode is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/PlaceOfUnloading/country = "O" AND<br />
/<span>&#42;</span>/Consignment/PlaceOfUnloading/location = "O"<br />
ELSE /<span>&#42;</span>/Consignment/PlaceOfUnloading/country = "R" AND<br />
/<span>&#42;</span>/Consignment/PlaceOfUnloading/location = "R"


## C0394

**Functional Description**

IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'Z'<br />
THEN<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt; = "R" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt; = "O" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'X'<br />
THEN<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt; = "R" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt; = "O" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'Y'<br />
THEN<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; = "R" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt; = "O" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'W'<br />
THEN<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt; = "R" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt; = "O" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'V'<br />
THEN<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt; = "R" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'U'<br />
THEN<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt; = "R" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt; = "N"AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt; = "O" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'T'<br />
THEN<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; = "N" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt; = "O" AND<br />
&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'Z'<br />
THEN<br />
/<span>&#42;</span>/Consignment/LocationOfGoods/Address = "R"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson = "O"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'X'<br />
THEN<br />
/<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator = "R"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson = "O"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'Y'<br />
THEN<br />
/<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber = "R"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson = "O"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'W'<br />
THEN<br />
/<span>&#42;</span>/Consignment/LocationOfGoods/GNSS = "R"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson = "O"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'V'<br />
THEN<br />
/<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice = "R"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'U'<br />
THEN<br />
/<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode = "R"<br />
AND/<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice = "N"<br />
AND/<span>&#42;</span>/Consignment/LocationOfGoods/GNSS = "N"<br />
AND/<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber = "N"<br />
AND/<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator = "N"<br />
AND/<span>&#42;</span>/Consignment/LocationOfGoods/Address = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson = "O"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'T'<br />
THEN<br />
/<span>&#42;</span>/Consignment/LocationOfGoods/Address = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator = "N"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson = "O"<br />
AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress = "R"


## C0396

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT.Code&gt; is EQUAL to ‘2’<br />
THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt; = "R"<br />
ELSE &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/code is EQUAL to ‘2’<br />
THEN /<span>&#42;</span>/Consignment/Incident/TransportEquipment/numberOfSeals = "R"<br />
ELSE /<span>&#42;</span>/Consignment/Incident/TransportEquipment/numberOfSeals = "O"


## C0400

**Functional Description**

IF &lt;COUNTRY-ACTION-UNAVAILABILITY.Type&gt; is EQUAL to ‘S’<br />
THEN &lt;COUNTRY-ACTION-UNAVAILABILITY.End date and time&gt; = "R"<br />
ELSE &lt;COUNTRY-ACTION-UNAVAILABILITY.End date and time&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/Country/Action/Unavailability/type is EQUAL to ‘S’<br />
THEN /<span>&#42;</span>/Country/Action/Unavailability/endDateAndTime = "R"<br />
ELSE /<span>&#42;</span>/Country/Action/Unavailability/endDateAndTime = "O"


## C0403

**Functional Description**

IF &lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to “D”<br />
THEN &lt;CONSIGNMENT-PLACE OF LOADING&gt; = “O”<br />
ELSE &lt;CONSIGNMENT-PLACE OF LOADING&gt; = “R”

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to “D”<br />
THEN /<span>&#42;</span>/Consignment/PlaceOfLoading = “O”<br />
ELSE /<span>&#42;</span>/Consignment/PlaceOfLoading = “R”


## C0404

**Functional Description**

IF &lt;CC015C-CONSIGNMENT-PLACE OF LOADING&gt; is PRESENT OR<br />
&lt;CC013C-CONSIGNMENT-PLACE OF LOADING&gt; is PRESENT<br />
THEN &lt;CC170C-CONSIGNMENT-PLACE OF LOADING&gt; = “O”<br />
ELSE &lt;CC170C-CONSIGNMENT-PLACE OF LOADING&gt; = “R”

**Technical Description**

IF (/CC015C/Consignment/PlaceOfLoading is PRESENT OR /CC013C/Consignment/PlaceOfLoading<br />
is PRESENT)<br />
THEN /CC170C/Consignment/PlaceOfLoading = “O”<br />
ELSE /CC170C/Consignment/PlaceOfLoading = “R”


## C0411

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br />
THEN &lt;TRANSIT OPERATION.TIR carnet number&gt; = "R"<br />
ELSE &lt;TRANSIT OPERATION.TIR carnet number&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br />
THEN /<span>&#42;</span>/TransitOperation/TIRCarnetNumber = "R"<br />
ELSE /<span>&#42;</span>/TransitOperation/TIRCarnetNumber = "N"


## C0417

**Functional Description**

IF &lt;GUARANTEE-GUARANTEE REFERENCE-INVALID GUARANTEE REASON.Code&gt; is EQUAL to<br />
‘G01’<br />
THEN &lt;GUARANTEE-GUARANTEE REFERENCE-CUSTOMS OFFICE OF GUARANTEE&gt; = "O"<br />
ELSE &lt;GUARANTEE-GUARANTEE REFERENCE-CUSTOMS OFFICE OF GUARANTEE&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/Guarantee/GuaranteeReference/InvalidGuaranteeReason/code&gt; is EQUAL to ‘G01’<br />
THEN /<span>&#42;</span>/Guarantee/GuaranteeReference/CustomsOfficeOfGuarantee = "O"<br />
ELSE /<span>&#42;</span>/Guarantee/GuaranteeReference/CustomsOfficeOfGuarantee = "R"


## C0440

**Functional Description**

IF &lt;CC043C-CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is NOT EQUAL to '0'<br />
OR &lt;CC043C-CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt; is NOT<br />
EQUAL to '0'<br />
THEN &lt;CC044C-UNLOADING REMARK.State of seals&gt; = "R"<br />
ELSE &lt;CC044C-UNLOADING REMARK.State of seals&gt; = "N"

**Technical Description**

IF /CC043C/Consignment/TransportEquipment/numberOfSeals is NOT EQUAL to '0'<br />
OR /CC043C/Consignment/Incident/TransportEquipment/numberOfSeals is NOT EQUAL to '0'<br />
THEN /CC044C/UnloadingRemark/stateOfSeals = "R"<br />
ELSE /CC044C/UnloadingRemark/stateOfSeals = "N"


## C0451

**Functional Description**

IF &lt;CC060C-TYPE OF CONTROLS.Type&gt; is EQUAL to '50'<br />
THEN &lt;CC060C-TYPE OF CONTROLS.Text&gt; = "R"<br />
ELSE &lt;CC500C-TYPE OF CONTROLS.Text&gt; = "O"

**Technical Description**

IF /CC060C/TypeOfControls/type is EQUAL to '50'<br />
THEN /CC060C/TypeOfControls/text = "R"<br />
ELSE /CC060C/TypeOfControls/text = "O"


## C0452

**Functional Description**

IF &lt;CC060C-TRANSIT OPERATION.Notification type&gt; is in SET {1, 2}<br />
THEN &lt;CC060C-TYPE OF CONTROLS&gt; = "N"<br />
ELSE &lt;CC060C-TYPE OF CONTROLS&gt; = "R"

**Technical Description**

IF /CC060C/TransitOperation/notificationType is in SET {1, 2}<br />
THEN /CC060C/TypeOfControls = "N"<br />
ELSE /CC060C/TypeOfControls = "R"


## C0455

**Functional Description**

IF &lt;CC060C-TransitOperation.Notification type&gt; is EQUAL to '1'<br />
THEN &lt;CC060C-REQUESTED DOCUMENT&gt; = "R"<br />
ELSE IF &lt;CC060C-TRANSIT OPERATION.Notification type&gt; is EQUAL to '0'<br />
THEN &lt;CC060C-REQUESTED DOCUMENT&gt; = "O"<br />
ELSE &lt;CC060C-REQUESTED DOCUMENT&gt; = "N"

**Technical Description**

IF /CC060C/TransitOperation/notificationType is EQUAL to '1'<br />
THEN /CC060C/RequestedDocument = "R"<br />
ELSE IF /CC060C/TransitOperation/notificationType is EQUAL to '0'<br />
THEN /CC060C/RequestedDocument = "O"<br />
ELSE /CC060C/RequestedDocument = "N"


## C0460

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Qualifier of identification&gt; is EQUAL to 'W'<br />
THEN<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION-GNSS&gt; = "R" AND<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION -ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Qualifier of identification&gt; is EQUAL to 'U'<br />
THEN<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION.UN LOCODE&gt;= "R" AND<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION-GNSS&gt; = "N" AND<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Qualifier of identification&gt; is EQUAL to 'Z'<br />
THEN<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS&gt; = "R" AND<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION.UN LOCODE&gt; = "N" AND<br />
&lt;CONSIGNMENT-INCIDENT-LOCATION-GNSS&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'W'<br />
THEN<br />
/<span>&#42;</span>/Consignment/Incident/Location/GNSS = "R" AND<br />
/<span>&#42;</span>/Consignment/Incident/Location/UNLocode = "N" AND<br />
/<span>&#42;</span>/Consignment/Incident/Location/Address = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'U'<br />
THEN<br />
/<span>&#42;</span>/Consignment/Incident/Location/UNLocode = "R" AND<br />
/<span>&#42;</span>/Consignment/Incident/Location/GNSS = "N" AND<br />
/<span>&#42;</span>/Consignment/Incident/Location/Address = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'Z'<br />
THEN<br />
/<span>&#42;</span>/Consignment/Incident/Location/Address = "R" AND<br />
/<span>&#42;</span>/Consignment/Incident/Location/UNLocode = "N" AND<br />
/<span>&#42;</span>/Consignment/Incident/Location/GNSS = "N"


## C0461

**Functional Description**

IF Message type of the rejected message is in SET <a href="../downloads/CL385.zip">CL385</a> (MessageTypeWithoutHeader)<br />
THEN &lt;CD906C-HEADER&gt; = "N"<br />
ELSE &lt;CD906C-HEADER&gt; = "R"

**Technical Description**

IF Message type of the rejected message is in SET <a href="../downloads/CL385.zip">CL385</a><br />
THEN /CD906C/Header = "N"<br />
ELSE /CD906C/Header = "R"


## C0466

**Functional Description**

IF&lt;TRANSIT OPERATION.Request rejection reason code&gt; is PRESENT<br />
THEN<br />
&lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; = "N" AND<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; = "N" AND<br />
&lt;RISK ANALYSIS IDENTIFICATION&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.TIR Carnet number&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.Specific circumstance indicator&gt; = "N" AND no validation of other conditions<br />
is performed<br />
ELSE the optionality of<br />
&lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; will be derived from other conditions AND<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; will be derived from other conditions<br />
AND<br />
&lt;RISK ANALYSIS IDENTIFICATION&gt; will be derived from other conditions AND<br />
&lt;TRANSIT OPERATION.TIR Carnet number&gt; will be derived from other conditions AND<br />
&lt;TRANSIT OPERATION.Specific circumstance indicator&gt; will be derived from other conditions

**Technical Description**

IF/<span>&#42;</span>/TransitOperation/requestRejectionReasonCode is PRESENT<br />
THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared = "N"<br />
AND /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared = “N"<br />
AND /<span>&#42;</span>/RiskAnalysisIdentification = "N"<br />
AND /<span>&#42;</span>/TransitOperation/tirCarnetNumber = "N"<br />
AND /<span>&#42;</span>/TransitOperation/specificCircumstanceIndicator = "N"<br />
AND no validation of other conditions is performed<br />
ELSE the optionality of<br />
/<span>&#42;</span>/CustomsOfficeOfTransitDeclared will be derived from other conditions AND<br />
/<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared will be derived from other conditions AND<br />
/<span>&#42;</span>/RiskAnalysisIdentification will be derived from other conditions AND<br />
/<span>&#42;</span>/TransitOperation/tirCarnetNumber will be derived from other conditions AND<br />
/<span>&#42;</span>/TransitOperation/specificCircumstanceIndicator will be derived from other conditions


## C0467

**Functional Description**

IF &lt;CC028C-TRANSIT OPERATION.Declaration acceptance date&gt; is PRESENT<br />
THEN<br />
&lt;TRANSIT OPERATION.MRN&gt; = "R" AND<br />
&lt;TRANSIT OPERATION.LRN&gt; = "N"<br />
ELSE &lt;TRANSIT OPERATION.MRN&gt; = "N" AND<br />
&lt;TRANSIT OPERATION.LRN&gt; = "R"

**Technical Description**

IF /CC028C/TransitOperation/declarationAcceptanceDate&gt; is PRESENT<br />
THEN<br />
/<span>&#42;</span>/TransitOperation/MRN = "R" AND<br />
/<span>&#42;</span>/TransitOperation/LRN = "N"<br />
ELSE /<span>&#42;</span>/TransitOperation/MRN = "N" AND<br />
/<span>&#42;</span>/TransitOperation/LRN = "R"


## C0489

**Functional Description**

IF the country code (first two characters) in the &lt;CC029C-CUSTOMS OFFICE OF<br />
DEPARTURE.Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a> (CountryCustomsSecurityAgreementArea)<br />
THEN &lt;CC029C-CONSIGNMENT-LOCATION OF GOODS&gt; = "O"<br />
ELSE &lt;CC029C-CONSIGNMENT-LOCATION OF GOODS&gt; = "R"

**Technical Description**

IF the first two characters of the /CC029C/CustomsOfficeOfDeparture/referenceNumber is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
THEN /CC029C/Consignment/LocationOfGoods = "O"<br />
ELSE /CC029C/Consignment/LocationOfGoods = "R"


## C0492

**Functional Description**

IF &lt;TRANSIT OPERATION.Rejection code&gt; is EQUAL to '4'<br />
THEN &lt;TRANSIT OPERATION.Rejection reason&gt; = "R"<br />
ELSE &lt;TRANSIT OPERATION.Rejection reason&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/rejectionCode is EQUAL to '4'<br />
THEN /<span>&#42;</span>/TransitOperation/rejectionReason = "R"<br />
ELSE /<span>&#42;</span>/TransitOperation/rejectionReason = "O"


## C0502

**Functional Description**

 IF &lt;CONSIGNMENT.Reference number UCR&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number<br />
UCR&gt; = "N" AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br />
ITEM.Reference number UCR&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number UCR&gt; is PRESENT<br />
   THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br />
   ITEM.Reference number UCR&gt; = "N"<br />
ELSE IF (&lt;CONSIGNMENT-TRANSPORT DOCUMENT&gt; is PRESENT OR<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT DOCUMENT&gt; is PRESENT)<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br />
 ITEM.Reference number UCR&gt; = "O"<br />
ELSE<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Reference number UCR&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/referenceNumberUCR is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR = "N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR<br />
= "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR is PRESENT<br />
   THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR<br />
   = "N"<br />
ELSE IF (/<span>&#42;</span>/Consignment/TransportDocument is PRESENT OR<br />
/<span>&#42;</span>/Consignment/HouseConsignment/TransportDocument is PRESENT)<br />
   THEN<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR<br />
   = "O"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR= "R"


## C0505

**Functional Description**

IF &lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS.Country&gt; is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a>(CountryWithoutZip)<br />
THEN &lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;CONSIGNMENT-CONSIGNOR-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a> (CountryWithoutZip)<br />
THEN &lt;CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;CONSIGNMENT-CONSIGNEE-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a> (CountryWithoutZip)<br />
THEN &lt;CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a> (CountryWithoutZip)<br />
THEN &lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
(CountryWithoutZip)<br />
THEN &lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
(CountryWithoutZip)<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
(CountryWithoutZip)<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;GUARANTOR-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a> (CountryWithoutZip)<br />
THEN &lt;GUARANTOR-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;GUARANTOR-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;GUARANTEE REFERENCE-GUARANTOR-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
(CountryWithoutZip)<br />
THEN &lt;GUARANTEE REFERENCE-GUARANTOR-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;GUARANTEE REFERENCE-GUARANTOR-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;GUARANTEE REFERENCE-GUARANTOR-AGENT IN COUNTRY OF COMPETENT<br />
AYTHORITY-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a> (CountryWithoutZip)<br />
THEN &lt;GUARANTEE REFERENCE-GUARANTOR-AGENT IN COUNTRY OF COMPETENT<br />
AYTHORITY-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;GUARANTEE REFERENCE-GUARANTOR-AGENT IN COUNTRY OF COMPETENT<br />
AYTHORITY-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;GUARANTEE REFERENCE-OWNER-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a> (CountryWithoutZip)<br />
THEN &lt;GUARANTEE REFERENCE-OWNER-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;GUARANTEE REFERENCE-OWNER-ADDRESS.Postcode&gt; = "R";<br />
IF &lt;CONSIGNMENT-CONSIGNEE (ACTUAL)-ADDRESS.Country&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
(CountryWithoutZip)<br />
THEN &lt;CONSIGNMENT-CONSIGNEE(ACTUAL)-ADDRESS.Postcode&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-CONSIGNEE(ACTUAL)-ADDRESS.Postcode&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/HolderOfTheTransitProcedure/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/HolderOfTheTransitProcedure/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/HolderOfTheTransitProcedure/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Consignment/Consignor/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/Consignor/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/Consignor/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Consignment/Consignee/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/Consignee/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/Consignee/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Consignment/Incident/Location/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/Incident/Location/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/Incident/Location/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Consignment/LocationOfGoods/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/LocationOfGoods/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/LocationOfGoods/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Guarantor/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Guarantor/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Guarantor/Address/postcode = "R";<br />
IF /<span>&#42;</span>/GuaranteeReference/Guarantor/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/GuaranteeReference/Guarantor/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/GuaranteeReference/Guarantor/Address/postcode = "R";<br />
IF /<span>&#42;</span>/GuaranteeReference/Guarantor/AgentInCountryOfCompetentAuthority/Address/country is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/GuaranteeReference/Guarantor/AgentInCountryOfCompetentAuthority/Address/postcode =<br />
"O"<br />
ELSE /<span>&#42;</span>/GuaranteeReference/Guarantor/AgentInCountryOfCompetentAuthority/Address/postcode =<br />
"R";<br />
IF /<span>&#42;</span>/GuaranteeReference/Owner/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/GuaranteeReference/Owner/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/GuaranteeReference/Owner/Address/postcode = "R";<br />
IF /<span>&#42;</span>/Consignment/ConsigneeActual/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/ConsigneeActual/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/ConsigneeActual/Address/postcode = "R"


## C0511

**Functional Description**

IF &lt;Message type&gt; is in SET <a href="../downloads/CL610.zip">CL610</a> (MessageWithCorrelationIdentifier)<br />
  THEN &lt;Correlation identifier&gt; = "R"<br />
ELSE IF &lt;Message type&gt; is in SET <a href="../downloads/CL385.zip">CL385</a> (MessageTypeWithoutHeader)<br />
  THEN &lt;Correlation identifier&gt; = "N"<br />
ELSE &lt;Correlation identifier&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/messageType is in SET <a href="../downloads/CL610.zip">CL610</a><br />
  THEN /<span>&#42;</span>/correlationIdentifier = "R"<br />
ELSE IF /<span>&#42;</span>/messageType is in SET <a href="../downloads/CL385.zip">CL385</a><br />
  THEN /<span>&#42;</span>/correlationIdentifier = "N"<br />
ELSE /<span>&#42;</span>/correlationIdentifier = "O"


## C0531

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br />
AND &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to ‘4’<br />
THEN<br />
&lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference number&gt; = "R"<br />
ELSE<br />
&lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference number&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1,2,3}<br />
AND /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to ‘4’<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber = "R"<br />
ELSE /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber = "O"


## C0542

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to '0' AND &lt;TRANSIT OPERATION. Reduced dataset<br />
indicator&gt; is EQUAL to '1'<br />
THEN<br />
&lt;CONSIGNMENT-CONSIGNOR&gt; = "N" AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; = "N"<br />
ELSE<br />
  IF &lt;CONSIGNMENT-CONSIGNOR&gt; is PRESENT<br />
  THEN<br />
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; = "N"<br />
  ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '0' AND /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator is<br />
EQUAL to '1'<br />
THEN<br />
/<span>&#42;</span>/Consignment/Consignor = "N" AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignor = "N"<br />
ELSE<br />
  IF /<span>&#42;</span>/Consignment/Consignor is PRESENT<br />
  THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignor = "N"<br />
   ELSE /<span>&#42;</span>/Consignment/HouseConsignment/Consignor = "O"


## C0569

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'<br />
THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT-SEAL&gt; = "R"<br />
ELSE&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT-SEAL&gt; = "N";<br />
IF &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'<br />
THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT-SEAL&gt; = "R"<br />
ELSE &lt;CONSIGNMENT-TRANSPORT EQUIPMENT-SEAL&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/TransportEquipment/numberOfSeals is GREATER than '0'<br />
THEN<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment/Seal = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment/Seal = "N";<br />
IF /<span>&#42;</span>/Consignment/TransportEquipment/numberOfSeals is GREATER than '0'<br />
THEN<br />
/<span>&#42;</span>/Consignment/TransportEquipment/Seal = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/TransportEquipment/Seal = "N"


## C0586

**Functional Description**

IF &lt;TRANSIT OPERATION.Binding itinerary&gt; is EQUAL to ‘1’<br />
THEN &lt;CONSIGNMENT-COUNTRY OF ROUTING OF CONSIGNMENT&gt; = "R"<br />
ELSE IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 2, 3}<br />
THEN &lt;CONSIGNMENT-COUNTRY OF ROUTING OF CONSIGNMENT&gt; = "R"<br />
ELSE &lt;CONSIGNMENT-COUNTRY OF ROUTING OF CONSIGNMENT&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/bindingItinerary is EQUAL to ‘1’<br />
THEN /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment = "R"<br />
ELSE IF /<span>&#42;</span>/Transit Operation/security is in SET {1, 2, 3}<br />
   THEN /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment = "R"<br />
ELSE /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment = "O"


## C0587

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt;is in SET {2,3}<br />
THEN   <br />
 IF the first two characters of at least one iteration of the &lt;CUSTOMS OFFICE OF TRANSIT<br />
DECLARED.Reference number&gt; is NOT in <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a>   <br />
 THEN &lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT DECLARED&gt; = "O"   <br />
 ELSE &lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT DECLARED&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {2,3}<br />
THEN<br />
IF the first two characters of at least one iteration of the<br />
/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
THEN /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared = "O"<br />
ELSE /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared = "N"


## C0598

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 3} AND<br />
the country code (first two characters) in the &lt;CUSTOMS OFFICE OF TRANSIT<br />
(DECLARED).Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a> (CountryCustomsSecurityAgreementArea)<br />
THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; = "R"<br />
ELSE &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 3} AND<br />
the first two characters of the /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated ="R"<br />
ELSE /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated = "O"


## C0599

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3} AND<br />
&lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to ‘A’<br />
THEN &lt;CONSIGNMENT.Mode of transport at the border&gt; = "R"<br />
ELSE &lt;CONSIGNMENT.Mode of transport at the border&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1,2,3} AND<br />
/<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to ‘A’<br />
THEN /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder = "R"<br />
ELSE /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder = "O"


## C0600

**Functional Description**

IF &lt;CC015C-TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br />
THEN &lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt; = "R"<br />
ELSE &lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt; = "O"

**Technical Description**

IF /CC015C/TransitOperation/security is in SET {1,2,3}<br />
THEN /CC170C/Consignment/modeOfTransportAtTheBorder = "R"<br />
ELSE /CC170C/Consignment/modeOfTransportAtTheBorder = "O"


## C0670

**Functional Description**

IF &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt; is PRESENT only once AND &lt;CONSIGNMENT-<br />
TRANSPORT EQUIPMENT.Container identification number&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT-GOODS REFERENCE&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-TRANSPORT EQUIPMENT-GOODS REFERENCE&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/TransportEquipment is PRESENT only once AND<br />
/<span>&#42;</span>/Consignment/TransportEquipment/containerIdentificationNumber is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/TransportEquipment/GoodsReference = "O"<br />
ELSE /<span>&#42;</span>/Consignment/TransportEquipment/GoodsReference = "R"


## C0671

**Functional Description**

IF &lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR.Identification number&gt; is<br />
PRESENT<br />
OR &lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-LOCATION OF GOODS.Additional identifier&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-LOCATION OF GOODS.Additional identifier&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator/identificationNumber is PRESENT<br />
OR /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/LocationOfGoods/additionalIdentifier = "O"<br />
ELSE /<span>&#42;</span>/Consignment/LocationOfGoods/additionalIdentifier = "N"


## C0685

**Functional Description**

IF &lt;CC028C-TRANSIT OPERATION.Declaration acceptance date&gt; is PRESENT<br />
THEN &lt;CC060C-TRANSIT OPERATION.MRN&gt; = "R" AND &lt;CC060C-TRANSIT OPERATION.LRN&gt; =<br />
"N"<br />
ELSE &lt;CC060C-TRANSIT OPERATION.MRN&gt; = "N" AND &lt;CC060C-TRANSIT OPERATION.LRN&gt; =<br />
"R"

**Technical Description**

IF /CC028C/TransitOperation/declarationAcceptanceDate is PRESENT<br />
THEN /CC060C/TransitOperation/MRN = "R" AND /CC060C/TransitOperation/LRN = "N"<br />
ELSE /CC060C/TransitOperation/MRN = "N" AND /CC060C/TransitOperation/LRN = "R"


## C0705

**Functional Description**

IF &lt;CC190C-TRANSIT OPERATION.AES communication purpose&gt; is EQUAL to '1'<br />
THEN &lt;TRANSIT OPERATION.LRN&gt; = "R" AND &lt;TRANSIT OPERATION.MRN&gt; = "N"<br />
ELSE &lt;TRANSIT OPERATION.LRN&gt; = "N" AND &lt;TRANSIT OPERATION.MRN&gt; = "R"

**Technical Description**

IF /CC190C/TransitOperation/AESCommunicationPurpose is EQUAL to '1'<br />
THEN /<span>&#42;</span>/TransitOperation/LRN = "R" AND /<span>&#42;</span>/TransitOperation/MRN = "N"<br />
ELSE /<span>&#42;</span>/TransitOperation/LRN = "N" AND /<span>&#42;</span>/TransitOperation/MRN = "R"


## C0707

**Functional Description**

IF &lt;CC190C-TRANSIT OPERATION.AES communication purpose&gt; is in SET {2, 3}<br />
THEN &lt;CC190C-TRANSIT OPERATION.Declaration acceptance date&gt; = "R"<br />
ELSE &lt;CC190C-TRANSIT OPERATION.Declaration acceptance date&gt; = "N"

**Technical Description**

IF /CC190C/TransitOperation/AESCommunicationPurpose is in SET {2, 3}<br />
THEN /CC190C/TransitOperation/declarationAcceptanceDate = "R"<br />
ELSE /CC190C/TransitOperation/declarationAcceptanceDate = "N"


## C0708

**Functional Description**

IF &lt;CC190C-TRANSIT OPERATION.AES communication purpose&gt; is EQUAL to '3'<br />
THEN &lt;CC190C-TRANSIT OPERATION.Amendment acceptance date and time&gt; = "R"<br />
ELSE &lt;CC190C-TRANSIT OPERATION.Amendment acceptance date and time&gt; = "N"

**Technical Description**

IF /CC190C/TransitOperation/AESCommunicationPurpose is EQUAL to '3'<br />
THEN /CC190C/TransitOperation/amendmentAcceptanceDateAndTime = "R"<br />
ELSE /CC190C/TransitOperation/amendmentAcceptanceDateAndTime = "N"


## C0710

**Functional Description**

IF &lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to 'D'<br />
THEN &lt;CONSIGNMENT-LOCATION OF GOODS&gt; = "O"<br />
ELSE IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br />
DEPARTURE.Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a>(CountryCustomsSecurityAgreementArea)<br />
THEN &lt;CONSIGNMENT-LOCATION OF GOODS&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-LOCATION OF GOODS&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/Additional declaration type is EQUAL to 'D'<br />
THEN /<span>&#42;</span>/Consignment/LocationOfGoods = "O"<br />
ELSE IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
THEN /<span>&#42;</span>/Consignment/LocationOfGoods = "O"<br />
ELSE /<span>&#42;</span>/Consignment/LocationOfGoods = "R"


## C0715

**Functional Description**

IF &lt;RISK ANALYSIS IDENTIFICATION.Code&gt; is EQUAL to ‘R’<br />
THEN<br />
   &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Code&gt; = "R" AND<br />
   &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Risk area code&gt; =<br />
"O"<br />
ELSE IF &lt;RISK ANALYSIS IDENTIFICATION.Code&gt; is EQUAL to 'X'<br />
   THEN<br />
   &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Code&gt; = “N”<br />
AND<br />
  &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Risk area code&gt;<br />
= "R"<br />
   ELSE<br />
  IF &lt;RISK ANALYSIS IDENTIFICATION.Code&gt; is EQUAL to 'Y')<br />
  THEN { at least one occurrence of<br />
  &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT&gt; (within any<br />
  &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS&gt;) with<br />
  { &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Code&gt; = "R"<br />
AND<br />
   &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Risk area<br />
code&gt; = "O"}}<br />
 AND<br />
  { at least one occurrence of<br />
   &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT&gt; = "R" (within<br />
any<br />
&lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS&gt;) with<br />
  { &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Code&gt; = "N"<br />
AND<br />
   &lt;RISK ANALYSIS IDENTIFICATION-RISK ANALYSIS-RISK ANALYSIS RESULT.Risk area<br />
code&gt; = "R"}}

**Technical Description**

IF /<span>&#42;</span>/RiskAnalysisIdentification/code is EQUAL to ‘R’<br />
THEN  /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/code = "R"<br />
  AND  /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/riskAreaCode = "O"<br />
ELSE IF /<span>&#42;</span>/RiskAnalysisIdentification/code is EQUAL to 'X'<br />
 THEN /<span>&#42;</span>/ RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/code = "N" AND<br />
   /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/riskAreaCode = "R"<br />
 ELSE<br />
 IF /<span>&#42;</span>/RiskAnalysisIdentification/code is EQUAL to 'Y'<br />
 THEN { at least one occurrence of<br />
/<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult (within any<br />
/<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis) with<br />
   { /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/code = "R" AND<br />
/<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/riskAreaCode = "O"}}<br />
  AND<br />
{ at least one occurrence of /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult<br />
(within any<br />
 /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis) with<br />
{ /<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/code = "N" AND<br />
/<span>&#42;</span>/RiskAnalysisIdentification/RiskAnalysis/RiskAnalysisResult/riskAreaCode = "R"}}


## C0716

**Functional Description**

IF &lt;CC906C-Message type&gt; is in SET {CC040C, CC042C, CC048C}<br />
THEN &lt;CC906C-HEADER.LRN&gt; = "N" and &lt;CC906C-HEADER.MRN&gt; = "R"<br />
ELSE IF &lt;CC906C-Message type&gt; is EQUAL to 'CC190C'<br />
THEN<br />
 IF &lt;CC190C-TRANSIT OPERATION.LRN&gt; is PRESENT<br />
 THEN &lt;CC906C-HEADER.LRN&gt; = "R" and &lt;CC906C-HEADER.MRN&gt; = "N"<br />
 ELSE &lt;CC906C-HEADER.LRN&gt; = "N" and &lt;CC906C-HEADER.MRN&gt; = "R"<br />
ELSE IF &lt;CC906C-Message type&gt; is EQUAL to 'CC191C' THEN<br />
IF &lt;CC191C-TRANSIT OPERATION.LRN&gt; is PRESENT<br />
THEN &lt;CC906C-HEADER.LRN&gt; = "R" and &lt;CC906C-HEADER.MRN&gt; = "N"<br />
ELSE &lt;CC906C-HEADER.LRN&gt; = "N" and &lt;CC906C-HEADER.MRN&gt; = "R"

**Technical Description**

IF /CC906C/messageType is in SET {CC040C, CC042C, CC048C}<br />
THEN /CC906C/Header/LRN = "N" and /CC906C/Header/MRN = "R"<br />
ELSE IF /CC906C/messageType is EQUAL to 'CC190C'<br />
THEN<br />
IF /CC190C/TransitOperation/LRN is PRESENT<br />
THEN /CC906C/Header/LRN = "R" and /CC906C/Header/MRN = "N"<br />
ELSE<br />
/CC906C/Header/LRN = "N" and /CC906C/Header/MRN = "R"<br />
ELSE IF /CC906C/messageType is EQUAL to 'CC191C' THEN<br />
IF /CC191C/TransitOperation/LRN is PRESENT<br />
   THEN CC906C/Header/LRN = "R" and /CC906C/Header/MRN = "N"<br />
ELSE CC906C/Header/LRN = "N" and /CC906C/Header/MRN = "R"


## C0803

**Functional Description**

IF &lt;CD903D-EVALUATED MESSAGE.Message Type&gt; is EQUAL to ‘CD411D’<br />
THEN &lt;CD903D-EVALUATED MESSAGE.Country&gt; = “R”<br />
   AND &lt;CD903D-EVALUATED MESSAGE.Year&gt; = “R”<br />
   AND &lt;CD903D-EVALUATED MESSAGE.Month&gt; = “R”<br />
ELSE &lt;CD903D-EVALUATED MESSAGE.Country&gt; = “O”<br />
   AND &lt;CD903D-EVALUATED MESSAGE.Year&gt; = “O”<br />
   AND &lt;CD903D-EVALUATED MESSAGE.Month&gt; = “O”

**Technical Description**

IF /CD903D/EvaluatedMessage/messageType is EQUAL to ‘CD411D’<br />
THEN /CD903D/EvaluatedMessage/country = “R”<br />
   AND /CD903D/EvaluatedMessage/year = “R”<br />
   AND /CD903D/EvaluatedMessage/month = “R”<br />
ELSE /CD903D/EvaluatedMessage/country = “O”<br />
   AND /CD903D/EvaluatedMessage/year = “O”<br />
   AND /CD903D/EvaluatedMessage/month = “O”


## C0804

**Functional Description**

IF &lt;CD903D-CONSISTENCY CHECKS WARNING.Warning code&gt; is in SET {P1001, P2001}<br />
THEN &lt;CD903D-CONSISTENCY CHECKS WARNING.Original attribute value&gt; = "R"<br />
ELSE &lt;CD903D-CONSISTENCY CHECKS WARNING.Original attribute value&gt; = "N"

**Technical Description**

IF /CD903D/ConsistencyChecksWarning/warningCode is in SET {P1001, P2001}<br />
THEN /CD903D/ConsistencyChecksWarning/originalAttributeValue = "R"<br />
ELSE /CD903D/ConsistencyChecksWarning/originalAttributeValue = "N"


## C0805

**Functional Description**

IF &lt;CD411D-SENDING COUNTRY-SYSTEM APPLICABILITY-STATISTICAL<br />
CHARACTERISTICS.Statistics type support&gt; is EQUAL to '1'<br />
THEN &lt;CD411D-SENDING COUNTRY-SYSTEM APPLICABILITY-STATISTICAL<br />
CHARACTERISTICS-SERIES ELEMENTS&gt; = "R"<br />
ELSE &lt;CD411D-SENDING COUNTRY-SYSTEM APPLICABILITY-STATISTICAL<br />
CHARACTERISTICS-SERIES ELEMENTS&gt; = "N"

**Technical Description**

IF /CD411D/SendingCountry/SystemApplicability/StatisticalCharacteristics/statisticsTypeSupport is<br />
EQUAL to '1'<br />
THEN /CD411D/SendingCountry/SystemApplicability/StatisticalCharacteristics/SeriesElements = "R"<br />
ELSE /CD411D/SendingCountry/SystemApplicability/StatisticalCharacteristics/SeriesElements = “N”


## C0806

**Functional Description**

IF &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '5'<br />
THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; = “N”<br />
ELSE<br />
IF (&lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3} AND<br />
&lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to ‘A’)<br />
THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; =”R”<br />
ELSE &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; = “O”

**Technical Description**

IF /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '5'<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “N”<br />
ELSE<br />
IF (/<span>&#42;</span>/TransitOperation/security is in SET {1,2,3} AND<br />
/<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to ‘A’)<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “R”<br />
ELSE /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “O”


## C0807

**Functional Description**

IF &lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '5'<br />
THEN &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; = “N”<br />
ELSE<br />
   IF &lt;CC015C-TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br />
   AND &lt;CC013C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is NOT<br />
   PRESENT<br />
   AND &lt;CC015C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is NOT<br />
   PRESENT<br />
  THEN &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; =”R”<br />
  ELSE &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; = “O”

**Technical Description**

IF /CC170C/Consignment/modeOfTransportAtTheBorder is EQUAL to '5'<br />
THEN /CC170C/Consignment/ActiveBorderTransportMeans = “N”<br />
ELSE<br />
IF /CC015C/TransitOperation/security is in SET {1,2,3}<br />
AND /CC013C/Consignment/ActiveBorderTransportMeans is NOT PRESENT<br />
AND /CC015C/Consignment/ActiveBorderTransportMeans is NOT PRESENT<br />
THEN /CC170C/Consignment/ActiveBorderTransportMeans = “R”<br />
ELSE /CC170C/Consignment/ActiveBorderTransportMeans = “O”


## C0808

**Functional Description**

IF &lt;CC015C-TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br />
  AND<br />
 &lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to ‘4’ (Air)<br />
THEN &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference<br />
number&gt; = "R"<br />
ELSE &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference<br />
number&gt; = "O"

**Technical Description**

IF /CC015C/TransitOperation/security is in SET {1,2,3}<br />
AND<br />
  /CC170C/Consignment/modeOfTransportAtTheBorder is EQUAL to ‘4’<br />
THEN /CC170C/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber = "R"<br />
ELSE /CC170C/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber = "O"


## C0810

**Functional Description**

IF &lt;CD001C-CONSIGNMEN -TRANSPORT EQUIPMENT.Number of seals is GREATER than '0'<br />
OR &lt;CD003C-CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals is GREATER than '0'<br />
OR &lt;CD003C-CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals is GREATER<br />
than '0'<br />
THEN &lt;CD018C-CONTROL RESULT.State of seals&gt; = "R"<br />
ELSE &lt;CD018C-CONTROL RESULT.State of seals&gt; = "O"

**Technical Description**

IF /CD001C/Consignment/TransportEquipment/numberOfSeals is GREATER than '0'<br />
OR /CD003C/Consignment/TransportEquipment/numberOfSeals is GREATER than '0'<br />
OR /CD003C/Consignment/Incident/TransportEquipment/numberOfSeals is GREATER than '0'<br />
THEN /CD018C/ControlResult/stateOfSeals = "R"<br />
ELSE /CD018C/ControlResult/stateOfSeals = "O"


## C0811

**Functional Description**

IF &lt;TRANSIT OPERATION.Request rejection reason code&gt; is EQUAL to '1'<br />
THEN &lt;CUSTOMS OFFICE OF DEPARTURE&gt; = "N"<br />
ELSE &lt;CUSTOMS OFFICE OF DEPARTURE&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/requestRejectionReasonCode is EQUAL to '1'<br />
THEN /<span>&#42;</span>/CustomsOfficeOfDeparture = "N"<br />
ELSE /<span>&#42;</span>/CustomsOfficeOfDeparture = "R"


## C0812

**Functional Description**

IF the last two characters of &lt;Message recipient&gt; is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
(CountryCustomsSecurityAgreementArea)<br />
THEN<br />
&lt;TRANSIT OPERATION.Specific circumstance indicator&gt; = "N" AND<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; = "N" AND<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (ACTUAL)&gt; = "N" AND<br />
&lt;CONSIGNMENT-CARRIER&gt; = "N" AND<br />
&lt;CONSIGNMENT-PLACE OF UNLOADING&gt; = "N" AND<br />
&lt;CONSIGNMENT-TRANSPORT CHARGES&gt; = "N"<br />
AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt; = "N"<br />
AND no validation of other conditions is performed<br />
 ELSE<br />
&lt;TRANSIT OPERATION.Specific circumstance indicator&gt; = "O" AND<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; = "O" AND<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (ACTUAL)&gt; = "O" AND<br />
&lt;CONSIGNMENT-CARRIER&gt; = "O" AND<br />
&lt;CONSIGNMENT-PLACE OF UNLOADING&gt; = "O" AND<br />
&lt;CONSIGNMENT-TRANSPORT CHARGES&gt; = "O"<br />
AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt; = "O"

**Technical Description**

IF the last 2 characters of /<span>&#42;</span>/messageRecipient is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
THEN /<span>&#42;</span>/TransitOperation/specificCircumstanceIndicator = "N"<br />
AND /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared = "N"<br />
AND /<span>&#42;</span>/CustomsOfficeOfExitForTransitActual = "N"<br />
AND /<span>&#42;</span>/Consignment/Carrier = "N"<br />
AND /<span>&#42;</span>/Consignment/PlaceOfUnloading = "N"<br />
AND /<span>&#42;</span>/Consignment/TransportCharges = "N"<br />
AND /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges = "N"<br />
AND no validation of other conditions is performed<br />
ELSE /<span>&#42;</span>/TransitOperation/specificCircumstanceIndicator = "O"<br />
AND /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared = "O"<br />
AND /<span>&#42;</span>/CustomsOfficeOfExitForTransitActual = "O"<br />
AND /<span>&#42;</span>/Consignment/Carrier = "O"<br />
AND /<span>&#42;</span>/Consignment/PlaceOfUnloading = "O"<br />
AND /<span>&#42;</span>/Consignment/TransportCharges = "O"<br />
AND /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges = "O"


## C0813

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 2, 3} AND the last two characters of &lt;Message<br />
sender&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
 (CountryCustomsSecurityAgreementArea) AND the last two characters of &lt;Message recipient&gt; is in<br />
SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
(CountryCustomsSecurityAgreementArea)<br />
THEN &lt;RISK ANALYSIS IDENTIFICATION&gt;= "R"<br />
ELSE IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to ‘0’ AND the last two characters of &lt;Message<br />
sender&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity) AND the last two characters of &lt;Message<br />
recipient&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity)<br />
THEN &lt;RISK ANALYSIS IDENTIFICATION&gt;= "R"<br />
ELSE IF the last two characters of &lt;Message sender&gt; is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
(CountryCodesCommunity) OR the last two characters of &lt;Message recipient&gt; is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
(CountryCodesCommunity)<br />
THEN &lt;RISK ANALYSIS IDENTIFICATION&gt; = "N"

**Technical Description**

IF the /<span>&#42;</span>/TransitOperation/security is in SET {1, 2, 3} AND the last two characters of /<span>&#42;</span>/messageSender<br />
is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a> AND the last two characters of /<span>&#42;</span>/messageRecipient is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
THEN /<span>&#42;</span>/RiskAnalysisIdentification = "R"<br />
ELSE IF the /<span>&#42;</span>/TransitOperation/security is EQUAL to ‘0’ AND the last two characters of<br />
/<span>&#42;</span>/messageSender is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> AND the last two characters of /<span>&#42;</span>/messageRecipient is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
THEN /<span>&#42;</span>/RiskAnalysisIdentification = "R"<br />
 ELSE IF the last two characters of /<span>&#42;</span>/messageSender is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> OR<br />
 the last two characters of /<span>&#42;</span>/messageRecipient is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
THEN /<span>&#42;</span>/RiskAnalysisIdentification = "N"


## C0815

**Functional Description**

IF at least one occurrence of &lt;GUARANTEE.Guarantee type&gt; is in SET {2, 9}<br />
THEN &lt;CONSIGNMENT&gt; = "R"<br />
ELSE &lt;CONSIGNMENT&gt; = "N"

**Technical Description**

IF at least one occurrence of /<span>&#42;</span>/Guarantee/guaranteeType is in SET {2, 9}<br />
THEN /<span>&#42;</span>/Consignment = "R"<br />
ELSE /<span>&#42;</span>/Consignment = "N"


## C0816

**Functional Description**

IF the &lt;CUSTOMS OFFICE OF DEPARTURE&gt; (for the CC017C) or the &lt;CUSTOMS OFFICE OF<br />
DESTINATION (ACTUAL)&gt; [for the CD018C and CC044C] is located in a CTC country or AD or SM<br />
THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY<br />
CODE.Combined nomenclature code&gt; = "N"<br />
ELSE<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY<br />
CODE.Combined nomenclature code&gt; = "O"

**Technical Description**

IF the /<span>&#42;</span>/CustomsOfficeOfDeparture (for the CC017C) or the /<span>&#42;</span>/CustomsOfficeOfDestinationActual [for<br />
the CD018C and CC044C] is located in a CTC country or AD or SM<br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br />
atureCode= "N"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br />
atureCode= "O"


## C0817

**Functional Description**

IF &lt;CC037C-GUARANTEE REFERENCE-GUARANTEE QUERY.Query identifier&gt; is in SET {2, 4}<br />
THEN &lt;CC037C-GUARANTEE REFERENCE-USAGE&gt; = "N"<br />
ELSE &lt;CC037C-GUARANTEE REFERENCE-USAGE&gt; = "O"

**Technical Description**

IF /CC037C/GuaranteeReference/GuaranteeQuery/queryIdentifier is in SET {2, 4}<br />
THEN /CC037C/GuaranteeReference/Usage = "N"<br />
ELSE /CC037C/GuaranteeReference/Usage = "O"


## C0818

**Functional Description**

IF &lt;CC034C-REQUESTER.Role&gt; is EQUAL to '1'<br />
THEN &lt;CC034C-GUARANTEE REFERENCE-OWNER&gt; = "N"<br />
ELSE &lt;CC034C-GUARANTEE REFERENCE-OWNER&gt; = "R"

**Technical Description**

IF /CC034C/Requester/role is EQUAL to '1'<br />
THEN /CC034C/GuaranteeReference/Owner = "N"<br />
ELSE /CC034C/GuaranteeReference/Owner = "R"


## C0820

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is EQUAL to '1' <br />
THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Container identification number&gt; =<br />
"R"<br />
ELSE<br />
&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Container identification number&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/Transhipment/containerIndicator is EQUAL to '1' <br />
THEN<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment/containerIdentificationNumber = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment/containerIdentificationNumber = "O"


## C0821

**Functional Description**

IF country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br />
number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
(CountryCodesCTC)<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br />
COMMODITY CODE.Combined nomenclature code&gt; = "N"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br />
COMMODITY CODE.Combined nomenclature code&gt; = "O"

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br />
atureCode = "N"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br />
atureCode = "O".


## C0822

**Functional Description**

IF &lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to 'D'<br />
THEN &lt;CONSIGNMENT.Container indicator&gt; = “O”<br />
ELSE &lt;CONSIGNMENT.Container indicator&gt; = “R”

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to 'D'<br />
THEN /<span>&#42;</span>/Consignment/containerIndicator = "O"<br />
ELSE /<span>&#42;</span>/Consignment/containerIndicator = "R"


## C0823

**Functional Description**

IF &lt;CONSIGNMENT.Container indicator&gt; is PRESENT<br />
THEN<br />
 IF &lt;CONSIGNMENT.Container indicator&gt; is EQUAL to ‘1’<br />
 THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt; = "R"<br />
 ELSE &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt; = "O"<br />
ELSE &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/containerIndicator is PRESENT<br />
THEN<br />
 IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to ‘1’<br />
 THEN /<span>&#42;</span>/Consignment/TransportEquipment = "R"<br />
 ELSE /<span>&#42;</span>/Consignment/TransportEquipment = "O"<br />
ELSE /<span>&#42;</span>/Consignment/TransportEquipment = "N"


## C0824

**Functional Description**

IF &lt;CC013C-TRANSIT OPERATION.Declaration type&gt; is PRESENT<br />
THEN<br />
  IF &lt;CC013C-CONSIGNMENT.Container indicator&gt; is PRESENT<br />
  THEN &lt;CC170C-CONSIGNMENT.Container indicator&gt; = “O”<br />
  ELSE &lt;CC170C-CONSIGNMENT.Container indicator&gt; = “R”<br />
ELSE<br />
  IF &lt;CC015C-CONSIGNMENT.Container indicator&gt; is PRESENT<br />
  THEN &lt;CC170C-CONSIGNMENT.Container indicator&gt; = “O”<br />
  ELSE &lt;CC170C-CONSIGNMENT.Container indicator&gt; = “R”

**Technical Description**

IF /CC013C/TransitOperation/declarationType is PRESENT<br />
THEN<br />
  IF /CC013C/Consignment/containerIndicator is PRESENT<br />
  THEN /CC170C/Consignment/containerIndicator = “O”<br />
  ELSE /CC170C/Consignment/containerIndicator = “R”<br />
ELSE<br />
  IF /CC015C/Consignment/containerIndicator is PRESENT<br />
  THEN /CC170C/Consignment/containerIndicator = “O”<br />
  ELSE /CC170C/Consignment/containerIndicator = “R”


## C0826

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '5'<br />
THEN<br />
&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = “N” AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "N"<br />
ELSE<br />
IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "N"<br />
ELSE &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '5'<br />
THEN<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans = “N” AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans = "N"<br />
ELSE<br />
IF /<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans = "O"


## C0828

**Functional Description**

IF &lt;COUNTRY-ACTION-UNAVAILABILITY.Functionality&gt; is in SET CL168<br />
(BusinessFunctionalityCode)<br />
THEN &lt;COUNTRY-ACTION-UNAVAILABILITY-FALLBACK&gt; = "O"<br />
ELSE &lt;COUNTRY-ACTION-UNAVAILABILITY-FALLBACK&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/Country/Action/Unavailability/functionality is in SET CL168<br />
THEN /<span>&#42;</span>/Country/Action/Unavailability/Fallback = "O"<br />
ELSE /<span>&#42;</span>/Country/Action/Unavailability/Fallback = "N"


## C0831

**Functional Description**

IF &lt;CUSTOMS OFFICE OF DESTINATION&gt; is PRESENT<br />
THEN<br />
&lt;CUSTOMS OFFICE OF TRANSIT&gt; = "N" AND<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT&gt; = "N"<br />
ELSE IF &lt;CUSTOMS OFFICE OF TRANSIT&gt; is PRESENT<br />
THEN<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT&gt; = "N"<br />
ELSE<br />
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT&gt; = "R"

**Technical Description**

IF /<span>&#42;</span>/CustomsOfficeOfDestination is PRESENT<br />
THEN /<span>&#42;</span>/CustomsOfficeOfTransit = "N" AND /<span>&#42;</span>/CustomsOfficeOfExitForTransit = "N"<br />
ELSE IF /<span>&#42;</span>/CustomsOfficeOfTransit is PRESENT<br />
THEN /<span>&#42;</span>/CustomsOfficeOfExitForTransit = "N"<br />
ELSE<br />
/<span>&#42;</span>/CustomsOfficeOfExitForTransit = "R"


## C0833

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '5'<br />
THEN &lt;CC170C-CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = “N” AND<br />
&lt;CC170C -.CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = "N"<br />
ELSE IF &lt;CC015C-CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt; is NOT PRESENT AND<br />
&lt;CC015C-CONSIGNMENT.HOUSE CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt; is NOT<br />
PRESENT AND &lt;CC013C-CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt; is NOT PRESENT<br />
AND &lt;CC013C-CONSIGNMENT.HOUSE CONSIGNMENT. DEPARTURE TRANSPORT MEANS&gt; is<br />
NOT<br />
PRESENT<br />
THEN<br />
   IF &lt;CC170C-CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br />
  THEN &lt;CC170C-CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE<br />
   TRANSPORT MEANS&gt;= "N"<br />
ELSE<br />
&lt;CC170C-CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; ="O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '5'<br />
THEN<br />
/CC170C/Consignment/DepartureTransportMeans = “N” AND<br />
/CC170C/Consignment/HouseConsignment/DepartureTransportMeans = “N”<br />
ELSE IF /CC015C/Consignment/DepartureTransportMeans is NOT PRESENT AND<br />
/CC015C/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT AND<br />
/CC013C/Consignment/DepartureTransportMeans is NOT PRESENT AND<br />
/CC013C/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT<br />
THEN<br />
IF /CC170C/Consignment/DepartureTransportMeans is PRESENT<br />
THEN /CC170C/Consignment/HouseConsignment/DepartureTransportMeans = "N"<br />
ELSE /CC170C/Consignment/HouseConsignment/DepartureTransportMeans = "O"


## C0837

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT. Type&gt; is EQUAL to ‘N830’<br />
THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br />
MEASURE.Net mass&gt; = "R"<br />
ELSE IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to ‘1’<br />
THEN<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br />
MEASURE.Net mass&gt; = "N"<br />
ELSE<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br />
MEASURE.Net mass&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/type is EQUAL to ‘N830’<br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "R"<br />
ELSE IF /<span>&#42;</span>/ TransitOperation/reducedDatasetIndicator is EQUAL to ‘1’<br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "N"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "O"


## C0839

**Functional Description**

IF &lt;AUTHORISATION.Type&gt; is NOT EQUAL to 'C521'<br />
THEN<br />
 &lt;TRANSIT OPERATION.Limit date&gt; = “N”<br />
ELSE<br />
IF &lt;Transit Operation/Additional declaration type&gt; is EQUAL to 'D'<br />
   THEN<br />
   &lt;TRANSIT OPERATION.Limit date&gt; = “O”<br />
ELSE<br />
  &lt;TRANSIT OPERATION.Limit date&gt; = “R”

**Technical Description**

IF /<span>&#42;</span>/Authorisation/type is NOT EQUAL to 'C521'<br />
THEN<br />
/<span>&#42;</span>/TransitOperation/limitDate = “N”<br />
ELSE<br />
   IF /<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to 'D'<br />
   THEN<br />
  /<span>&#42;</span>/TransitOperation/limitDate = “O”<br />
ELSE<br />
   /<span>&#42;</span>/TransitOperation/limitDate = “R”


## C0840

**Functional Description**

IF &lt;CC015C-AUTHORISATION.Type&gt; is NOT EQUAL to 'C521' OR &lt;CC013C-<br />
AUTHORISATION.Type&gt; is NOT EQUAL to 'C521'<br />
THEN &lt;CC170C-TRANSIT OPERATION.Limit date&gt; = "N"<br />
ELSE<br />
IF &lt;CC015C-TRANSIT OPERATION.Limit date&gt; is NOT PRESENT AND &lt;CC013C-TRANSIT<br />
OPERATION.Limit date&gt; is NOT PRESENT<br />
THEN &lt;CC170C-TRANSIT OPERATION.Limit date&gt; = "R"<br />
ELSE &lt;CC170C-TRANSIT OPERATION.Limit date&gt; = "O"

**Technical Description**

IF /CC015C/Authorisation/type is NOT EQUAL to 'C521' OR /CC013C/Authorisation/type is NOT<br />
EQUAL to 'C521'<br />
THEN /CC170C/TransitOperation/limitDate = “N”<br />
ELSE<br />
IF /CC015C/TransitOperation/limitDate is NOT PRESENT AND /CC013C/TransitOperation/limitDate is<br />
NOT PRESENT<br />
THEN /CC170C/TransitOperation/limitDate = “R”<br />
ELSE /CC170C/TransitOperation/limitDate = “O”


## C0844

**Functional Description**

IF &lt;CD001C-CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; OR<br />
&lt;CD003C-CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; is EQUAL to<br />
‘N830’<br />
THEN<br />
&lt;CC025C -CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br />
MEASURE.Net mass&gt; = "R"<br />
ELSE IF &lt;CD001C- TRANSIT OPERATION.Reduced dataset indicator&gt; OR &lt;CD003C- TRANSIT<br />
OPERATION.Reduced dataset indicator&gt; is EQUAL to ‘1’<br />
THEN<br />
&lt;CC025C -CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br />
MEASURE.Net mass&gt; = "N"<br />
ELSE<br />
&lt;CC025C -CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br />
MEASURE.Net mass&gt; = "O"

**Technical Description**

IF /CD001C/Consignment/HouseConsignment/PreviousDocument/Type OR IF / CD003C<br />
/Consignment/HouseConsignment/PreviousDocument/Type is EQUAL to ‘N830’<br />
THEN<br />
/CC025C/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass =<br />
"R"<br />
ELSE IF /CD001C/TransitOperation/reducedDatasetIndicator OR<br />
/CD003C/TransitOperation/reducedDatasetIndicator is EQUAL to ‘1’<br />
THEN<br />
/CC025C/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass =<br />
"N"<br />
ELSE<br />
/CC025C/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass =<br />
"O"


## C0860

**Functional Description**

IF &lt;TRANSIT OPERATION.AES Communication purpose&gt; is EQUAL to '2'<br />
THEN &lt;CONSIGNMENT&gt; = "N"<br />
ELSE &lt;CONSIGNMENT&gt; = "R"

**Technical Description**

IF /CC190C/TransitOperation/AESCommunicationPurpose&gt; is EQUAL to '2'<br />
THEN /CC190C/Consignment = "N"<br />
ELSE /CC190C/Consignment = "R"


## C0861

**Functional Description**

IF (&lt;CC015C-AUTHORISATION.Type&gt; is EQUAL to 'C521' AND &lt;CC015C -CONSIGNMENT-<br />
LOCATION OF GOODS&gt; is PRESENT (either from CC015C or from Authorisation record))<br />
 OR (&lt;CC013C-AUTHORISATION.Type&gt; is EQUAL to 'C521' AND &lt;CC013C- CONSIGNMENT-<br />
LOCATION OF GOODS&gt; is PRESENT (either from CC013C or from Authorisation record))<br />
THEN &lt;CC190C-CONSIGNMENT-LOCATION OF GOODS&gt; = "R"<br />
ELSE &lt;CC190C-CONSIGNMENT-LOCATION OF GOODS&gt; = "N"

**Technical Description**

IF (/CC015C/Authorisation/type is EQUAL to 'C521' AND /CC015C/Consignment/LocationOfGoods is<br />
PRESENT (either from CC015C or from Authorisation record))<br />
 OR (/CC013C/Authorisation/type is EQUAL to 'C521' AND<br />
/CC013C/Consignment/LocationOfGoods is PRESENT (either from CC013C or from Authorisation<br />
record))<br />
THEN /CC190C/Consignment/LocationOfGoods = "R"<br />
ELSE /CC190C/Consignment/LocationOfGoods = "N"


## C0862

**Functional Description**

IF (&lt;CC015C-CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-SUPPORTING<br />
DOCUMENT.Type&gt; is in SET {C651,C658}<br />
OR &lt;CC013C-CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-SUPPORTING<br />
DOCUMENT.Type&gt; is in SET {C651,C658}) AND (&lt;CC015C-CONSIGNMENT-HOUSE<br />
CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS MEASURE. Supplementary units&gt; is<br />
PRESENT<br />
OR &lt;CC013C-CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br />
GOODS MEASURE. Supplementary units&gt; is PRESENT)<br />
THEN &lt;CC190C-CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br />
GOODS MEASURE. Supplementary units&gt; = "R"<br />
ELSE &lt;CC190C-CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br />
GOODS MEASURE. Supplementary units&gt; = "N"

**Technical Description**

IF (/CC015C/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/type is in SET<br />
{C651, C658}<br />
OR /CC013C/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/type is in SET<br />
{C651,C658})<br />
AND (/CC015C/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br />
GoodsMeasure/supplementaryUnits is PRESENT OR<br />
/CC013C/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br />
GoodsMeasure/supplementaryUnits is PRESENT)<br />
THEN<br />
/CC190C/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br />
GoodsMeasure/supplementaryUnits = "R"<br />
ELSE<br />
/CC190C/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br />
GoodsMeasure/supplementaryUnits = "N”


## C0867

**Functional Description**

IF &lt;CD501C-HOLDER OF THE TRANSIT PROCEDURE&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a> (DocumentTypeExcise)<br />
  THEN &lt;CC191C-AES RESULTS-EXPORT OPERATION-GOODS SHIPMENT&gt; = "R"<br />
ELSE &lt;CC191C-AES RESULTS-EXPORT OPERATION-GOODS SHIPMENT&gt; = "N"

**Technical Description**

IF /CD501C/GoodsShipment/GoodsItem/PreviousDocument/type is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a><br />
   THEN /CC191C/AESResults/ExportOperation/GoodsShipment = "R"<br />
ELSE /CC191C/AESResults/ExportOperation/GoodsShipment = "N"


## C0870

**Functional Description**

IF the first three characters of &lt;Message recipient&gt; is EQUAL to ‘NTA’<br />
THEN &lt;INVALIDATION.Decision date and time&gt; = "N"<br />
ELSE &lt;INVALIDATION.Decision date and time&gt; =   "R"

**Technical Description**

IF the first three characters of /<span>&#42;</span>/messageRecipient is EQUAL to ‘NTA’<br />
THEN /<span>&#42;</span>/Invalidation/decisionDateAndTime = "N"<br />
ELSE /<span>&#42;</span>/Invalidation/decisionDateAndTime = "R"


## C0872
  
  **Functional Description**
  
  IF &lt;CONSIGNMENT.Container indicator&gt; is EQUAL to ‘1’<br />
THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt; = "R"<br />
 ELSE &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt; = "O"
  
  **Technical Description**
  
  IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to '1'<br />
THEN /<span>&#42;</span>/Consignment/TransportEquipment = "R"<br />
 ELSE /<span>&#42;</span>/Consignment/TransportEquipment = "O"
  

## C0904

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is PRESENT<br />
THEN<br />
IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br />
THEN &lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt; = "R"<br />
ELSE &lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt; = "N"<br />
ELSE<br />
IF &lt;CC015C-TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR' OR &lt;CC013C-TRANSIT<br />
OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br />
THEN &lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt; = "R"<br />
ELSE &lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is PRESENT<br />
THEN IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br />
   THEN /<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "R"<br />
   ELSE /<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "N"<br />
ELSE IF /CC015C/TransitOperation/declarationType is EQUAL to 'TIR' OR<br />
/CC013C/TransitOperation/declarationType is EQUAL to 'TIR'<br />
 THEN /<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "R"<br />
 ELSE /<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber = "N"


## C0908

**Functional Description**

IF &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '5'<br />
THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; = “N”<br />
ELSE<br />
IF &lt;TRANSIT OPERATION.Security is in SET {1,2,3}<br />
THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; =”R”<br />
ELSE &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; = “O”

**Technical Description**

IF /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '5'<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “N”<br />
ELSE<br />
IF /<span>&#42;</span>/TransitOperation/security is in SET {1,2,3}<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “R”<br />
ELSE /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “O”


## C0909

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br />
THEN<br />
IF &lt;CONSIGNMENT.Country of dispatch&gt; is PRESENT<br />
THEN<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt; = "N" AND<br />
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of<br />
dispatch&gt; = "N"<br />
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt; is<br />
PRESENT<br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of dispatch&gt; =<br />
"N"<br />
 ELSE<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of dispatch&gt; = "R"<br />
ELSE<br />
 &lt;CONSIGNMENT.Country of dispatch&gt; = "N" AND<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt; = "N" AND<br />
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of dispatch&gt; = "N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br />
THEN<br />
IF /<span>&#42;</span>/Consignment/countryOfDispatch is PRESENT<br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch = "N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch is PRESENT<br />
THEN<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"<br />
 ELSE<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/countryOfDispatch= "N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch = "N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"


## C0930

**Functional Description**

IF &lt;CONTROL RESULT.Code&gt; is in SET {B1, A5}<br />
THEN<br />
(&lt;CONSIGMENT&gt; = “R” AND &lt;TRANSIT OPERATION.Other things to report&gt; = “O”) OR<br />
(&lt;CONSIGMENT&gt; = “O” AND &lt;TRANSIT OPERATION.Other things to report&gt; = “R”)<br />
ELSE<br />
&lt;CONSIGMENT&gt; = “N” AND &lt;TRANSIT OPERATION.Other things to report&gt; = “O”

**Technical Description**

IF /<span>&#42;</span>/ControlResult/code is in SET {B1, A5}<br />
THEN<br />
(/<span>&#42;</span>/Consignment = “R” AND /<span>&#42;</span>/TransitOperation/otherThingsToReport = “O” ) OR (/<span>&#42;</span>/Consignment = “O”<br />
AND /<span>&#42;</span>/TransitOperation/otherThingsToReport = “R”)<br />
ELSE<br />
/<span>&#42;</span>/Consignment = “N” AND /<span>&#42;</span>/TransitOperation/otherThingsToReport = “O”
