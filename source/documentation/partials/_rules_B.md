## B1000

**Functional Description**

Guideline for Export followed by Transit & Groupage:<br /><br />
During the Transitional Period, in case of "Export Followed by Transit" with multiple export declarations
covered by one standard transit declaration (i.e. not a pre-lodged transit declaration), the D.G.
SUPPORTING DOCUMENT at CONSIGNMENT ITEM level can include the MRN of the related Export
declaration (maximum one Export MRN included per on Consignment item).

**Technical Description**

N/A


## B1016

**Functional Description**

During the Transitional Period, the data item “Customs office at border reference number”, is required
for ‘native CC015C’ and ‘native CC013C’ and optional if CC013C or CC015C is the outcome of the
upgraded CC013B or CC015B respectively. After the end of the Transitional Period, the data item will
be always required.

**Technical Description**

N/A


## B1091

**Functional Description**

During the Transitional Period (TP), the native CC015C, CC013C and CC170C sent to the National
Transit Application should not include the value ‘99’. This value ‘99’ is valid in <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a> during TP, only in
case the value ‘99’ is the result of the upgrade by the National Transit Application of a legacy message
(e.g. CC015B upgraded into CC015C).

**Technical Description**

N/A


## B1804

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0710 attached to /<span>&#42;</span>/Consignment/LocationOfGoods<br />
shall be disabled AND<br />
/<span>&#42;</span>/Consignment/LocationOfGoods = "O"


## B1805

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0837 will be disabled AND<br />
  IF /<span>&#42;</span>/ TransitOperation/reducedDatasetIndicator is EQUAL TO ‘1’<br />
 THEN<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "N"<br />
  ELSE<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass = "O"


## B1806

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0806 will be disabled AND<br />
IF /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is PRESENT<br />
THEN<br />
   IF /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '5' or '2'<br />
   THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “O”<br />
   ELSE /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “R”<br />
ELSE<br />
/<span>&#42;</span>/Consignment/ActiveBorderTransportMeans = “O”


## B1811

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0076 attached to<br />
/<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/identificationNumber<br />
will be disabled


## B1813

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0003 and R0006 shall be disabled.


## B1814

**Functional Description**

N/A.

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R3061 attached to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalInformation/code<br />
shall be disabled


## B1815

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0473 attached to<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans/identificationNumber<br />
will be disabled


## B1819

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0219 attached to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages<br />
shall be disabled


## B1820

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "R"<br />
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
THEN THIS /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "R"<br />
ELSE IF /<span>&#42;</span>/TransitOperation/security is in SET {0,1}<br />
THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "O"<br />
ELSE IF at least one instance of /<span>&#42;</span>/Consignment/AdditionalInformation/code is EQUAL to '30600'<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"<br />
ELSE IF at least one instance of<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalInformation/code is EQUAL to '30600'<br />
THEN THIS /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"<br />
ELSE IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "R"


## B1821

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/identificationNumber is<br />
PRESENT AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/identificationNumber is a valid<br />
identifier in the European EOS ((Economic Operators Systems) verified by the EU Member State<br />
receiving or sending this message), OR is a valid identifier in the DB of the CTC country receiving or<br />
sending this message<br />
THEN<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/name="N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address="N"<br />
ELSE<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/name="R" AND<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address="R";


## B1822

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/country is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip">CL505</a><br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/postcode = "O"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee/Address/postcode = "R";


## B1823

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0001 shall be disabled AND<br />
IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
THEN IF at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee is present<br />
THEN /<span>&#42;</span>/Consignment/Consignee = "N"<br />
ELSE /<span>&#42;</span>/Consignment/Consignee = "R"<br />
ELSE IF /<span>&#42;</span>/TransitOperation/security is in SET {2,3}<br />
THEN IF at least one instance of<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalInformation/code is EQUAL to '30600'<br />
THEN /<span>&#42;</span>/Consignment/Consignee = "N"<br />
ELSE /<span>&#42;</span>/Consignment/Consignee = "O"


## B1831

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0598 shall be disabled AND<br />
IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3} AND<br />
the first two characters of the /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
AND the first two characters of<br />
/<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; = "R"<br />
ELSE &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; = "O"


## B1832

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0106 attached to /<span>&#42;</span>/Consignment/TransportEquipment/numberOfSeals<br />
shall be disabled;<br />
IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0106 attached to /CD038C/Consignment/Incident/TransportEquipment/numberOfSeals<br />
shall be disabled.


## B1833

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0511 attached to /<span>&#42;</span>/correlationIdentifier shall be disabled<br />
AND /<span>&#42;</span>/correlationIdentifier = "O"


## B1834

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0153 attached to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode<br />
shall be disabled and the D.G. will become optional


## B1838

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
   IF /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/nationality is PRESENT OR<br />
   /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '2'<br />
  THEN<br />
 /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/typeOfIdentification = "R" AND<br />
 /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/identificationNumber = "R"<br />
   ELSE<br />
   /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/typeOfIdentification = "O" AND<br />
  /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/identificationNumber = "O"


## B1848

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0586 attached to /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment shall be disabled AND<br />
IF /<span>&#42;</span>/Transit Operation/security is in SET {1, 2, 3}<br />
THEN /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment = "R"<br />
ELSE /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment = "N"


## B1850

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF first digit of /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is in SET {2}<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/nationality="O"<br />
ELSE /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/nationality="R"


## B1858

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0191 will be disabled<br />
AND<br />
IF /<span>&#42;</span>/TransitOperation/security is EQUAL to ‘0’<br />
THEN /<span>&#42;</span>/Consignment/PlaceOfUnloading = “N”<br />
ELSE<br />
IF /<span>&#42;</span>/TransitOperation/specificCircumstanceIndicator is EQUAL to ‘XXX’<br />
THEN /<span>&#42;</span>/Consignment/PlaceOfUnloading = “O”<br />
ELSE /<span>&#42;</span>/Consignment/PlaceOfUnloading = "R"


## B1860

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0221 attached to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass shall be<br />
disabled


## B1862

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0223 attached to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass will be<br />
disabled.


## B1875

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '0' OR<br />
/<span>&#42;</span>/Consignment/TransportCharges is PRESENT<br />
THEN<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/TransportCharges = "N"<br />
ELSE<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/TransportCharges = "O".


## B1877

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt; THEN<br />
  IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee is PRESENT<br />
  for all /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br />
  THEN at least one occurrence of<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee must be different<br />
  from the others;<br />
IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt; THEN<br />
  IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/TransportCharges is<br />
  PRESENT for all /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br />
  THEN at least one occurrence of<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/TransportCharges must be<br />
   different from the others.


## B1889

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0599 will be disabled AND<br />
   IF/<span>&#42;</span>/TransitOperation/security is in SET {1,2,3} AND the first two characters of<br />
/<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is not in <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
   THEN<br />
/<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder = "R"<br />
   ELSE<br />
/<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder = "O"


## B1890

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0855 will be disabled<br />
AND<br />
IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to ‘3’<br />
THEN the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans can be up to '3x'<br />
ELSE the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans is '1x'


## B1891

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0826 shall be disabled AND<br />
IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '5'<br />
THEN<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans = “N”<br />
ELSE IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to ‘1’<br />
THEN<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans = “O”<br />
ELSE<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans = “R”


## B1892

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to ‘1’<br />
THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/identificationNumber = “O” AND<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification = “O”<br />
ELSE /<span>&#42;</span>/Consignment/DepartureTransportMeans/identificationNumber = “R” AND<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification = “R”


## B1893

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0403 will be disabled<br />
AND<br />
IF /<span>&#42;</span>/TransitOperation/security is EQUAL to ‘0’<br />
THEN /<span>&#42;</span>/Consignment/PlaceOfLoading = “N”<br />
ELSE /<span>&#42;</span>/Consignment/PlaceOfLoading = “R”


## B1895

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0502 shall be disabled AND<br />
   IF /<span>&#42;</span>/Consignment/referenceNumberUCR is PRESENT<br />
THEN<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "N"<br />
   ELSE<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR = "O"


## B1896

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 2, 3}<br />
THEN<br />
  IF /<span>&#42;</span>/Consignment/referenceNumberUCR is NOT PRESENT AND<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR is NOT<br />
  PRESENT<br />
   AND /<span>&#42;</span>/TransitOperation/declarationType is NOT EQUAL to ‘TIR’<br />
  THEN<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem[1]/TransportDocument = ''R''<br />
  ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/TransportDocument = ''O''


## B1897

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to ‘2’<br />
THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/nationality = "N"<br />
ELSE<br />
IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to ‘1’<br />
THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/nationality = “O”<br />
ELSE /<span>&#42;</span>/Consignment/DepartureTransportMeans/nationality = “R”


## B1898

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN<br />
IF /<span>&#42;</span>/Guarantee/GuaranteeReference/amountToBeCovered is PRESENT<br />
THEN /<span>&#42;</span>/Guarantee/GuaranteeReference/currency = "R"<br />
ELSE /<span>&#42;</span>/Guarantee/GuaranteeReference/currency = "N’’


## B1903

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0004 will be disabled


## B1904

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0005 will be disabled


## B1919

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0220 attached to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages<br />
shall be disabled


## B1922

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0601 will be disabled AND<br />
IF /<span>&#42;</span>/Consignment/HouseConsingment/ConsignmentItem/AdditionalReference/type is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a><br />
(DocumentTypeExcise) (i.e. Export of excise goods followed by transit (EMCS&AES+NCTS))<br />
THEN<br />
   IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/type is EQUAL to<br />
‘N830’<br />
   THEN<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is EQUAL to ‘T1’<br />
ELSE /<span>&#42;</span>/TransitOperation/declarationType is in SET {T1,TIR}<br />
   ELSE // no further constraints on ‘Declaration type’ data items<br />
ELSE<br />
   IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/type is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a><br />
(DocumentTypeExcise) (i.e. Transit movement of EU goods under excise suspension (EMCS+NCTS))<br />
   THEN<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/type is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2, T2F}<br />
ELSE /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F}


## B1964

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN R0364 attached to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages<br />
shall be disabled


## B1965

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0909 attached to /<span>&#42;</span>/Consignment/countryOfDispatch AND<br />
to /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch AND<br />
to /<span>&#42;</span>/ConsignmentHouseConsignment/ConsignmentItem/countryOfDispatch<br />
shall be disabled<br />
AND<br />
IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br />
THEN<br />
IF /<span>&#42;</span>/Consignment/countryOfDispatch is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch = "N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"<br />
ELSEIF /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch is PRESENT<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"<br />
ELSE /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "R"<br />
ELSE<br />
/<span>&#42;</span>/Consignment/countryOfDispatch= "N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch = "N" AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch = "N"


## B1966

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is LESS than or EQUAL to &lt;TPendDate&gt;<br />
THEN C0587 will be disabled<br />
IF /<span>&#42;</span>/TransitOperation/security is in SET {2,3}<br />
THEN<br />
  IF the first two characters of at least one iteration of the<br />
/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is NOT in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip">CL147</a><br />
  THEN /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared = "O"<br />
   ELSE /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared = "N"


## B2101

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/TransitOperation/arrivalDateAndTime (actual) = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/TransitOperation/recoveryCommunicationDate = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/FunctionalError/errorReason = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/GuaranteeReference/Guarantor/Address/country = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/GuaranteeReference/Guarantor/identificationNumber = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/CustomsOfficeOfDeparture = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass =<br />
"R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Recovery/text = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Guarantee/GuaranteeReference/amountToBeCovered = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /CD038C/Consignment/Incident/Endorsement/authority = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /CD038C/Consignment/Incident/Endorsement/place= "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/PlaceOfLoading = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/customsOfficeAtBorderReferenceNumber = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/nationality= "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/typeOfIdentification =”R”;<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/identificationNumber = "R";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification = “R”;<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/identificationNumber = “R”;<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/nationality = “R”;<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Guarantee/GuaranteeReference/currency = "R"


## B2400

**Functional Description**

N/A

**Technical Description**

IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/Incident = "N";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Enquiry/returnCopyReturnedDate = "N";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Consignee = "N";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/TransportDocument = "N";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/TransportCharges = "N";<br />
IF &lt;Decisive Date&gt; is GREATER than &lt;TPendDate&gt;<br />
THEN /<span>&#42;</span>/GuaranteeReference/Guarantor/contactDetailsInCountryOfCompetentAuthority = "N”.
