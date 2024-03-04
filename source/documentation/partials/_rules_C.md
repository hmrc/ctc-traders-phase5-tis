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
packages&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackagesUnpacked.zip">CL182</a> (KindOfPackagesUnpacked)<br />
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
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackagesUnpacked.zip">CL182</a><br />
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

IF &lt;Message type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageWithCorrelationIdentifier.zip">CL610</a> (MessageWithCorrelationIdentifier)<br />
  THEN &lt;Correlation identifier&gt; = "R"<br />
ELSE IF &lt;Message type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageTypeWithoutHeader.zip">CL385</a> (MessageTypeWithoutHeader)<br />
  THEN &lt;Correlation identifier&gt; = "N"<br />
ELSE &lt;Correlation identifier&gt; = "O"

**Technical Description**

IF /<span>&#42;</span>/messageType is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageWithCorrelationIdentifier.zip">CL610</a><br />
  THEN /<span>&#42;</span>/correlationIdentifier = "R"<br />
ELSE IF /<span>&#42;</span>/messageType is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageTypeWithoutHeader.zip">CL385</a><br />
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
