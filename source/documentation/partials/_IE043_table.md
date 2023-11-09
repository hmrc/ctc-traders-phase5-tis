<table cellspacing="0">
<tr>
<th>
   Field Name
  </th>
<th>
   Priority
  </th>
<th>
   Format / Max Repeat
  </th>
<th>
   Code Lists
  </th>
<th>
   Rules
  </th>
</tr>
<tr>
    <td><strong>MESSAGE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Message sender</td>
    <td>R</td>
    <td>an..35 (see <a href="../#message-sender-and-recipient-guidelines">Message sender and recipient guidelines</a>)</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Message recipient</td>
    <td>R</td>
    <td>an..35 (see <a href="../#message-sender-and-recipient-guidelines">Message sender and recipient guidelines</a>)</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>- Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Message type</td>
    <td>R</td>
    <td>an6</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageTypes.zip">CL060</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0511">C0511</a><br /><a href="rules-r.html#r0008">R0008</a></td>
</tr><tr>
    <td><strong>- TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-- Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationType.zip">CL231</a></td>
    <td><a href="rules-c.html#c0027">C0027</a><br /><a href="rules-r.html#r0601">R0601</a><br /><a href="rules-r.html#r0909">R0909</a><br /><a href="rules-r.html#r0911">R0911</a></td>
</tr><tr>
    <td>-- Declaration acceptance date</td>
    <td>D</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0027">C0027</a><br /><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-- Security</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeSecurity.zip">CL217</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Reduced dataset indicator</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDestination.zip">CL172</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0027">C0027</a></td>
</tr><tr>
    <td>-- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0120">G0120</a><br /><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td>-- TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0904">C0904</a><br /><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- ADDRESS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>--- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td><strong>- CTL_CONTROL</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Continue unloading</td>
    <td>R</td>
    <td>n1</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0510">G0510</a></td>
</tr><tr>
    <td><strong>- CONSIGNMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0027">C0027</a></td>
</tr><tr>
    <td>-- Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0343">C0343</a></td>
</tr><tr>
    <td>-- Container indicator</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Inland mode of transport</td>
    <td>O</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip">CL218</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Gross mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0027">C0027</a><br /><a href="rules-r.html#r0994">R0994</a></td>
</tr><tr>
    <td><strong>-- CONSIGNOR</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td>--- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td><strong>--- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>---- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>---- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0001">C0001</a><br /><a href="rules-g.html#g0001">G0001</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0851">R0851</a></td>
</tr><tr>
    <td>--- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td><strong>--- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>---- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>---- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0872">C0872</a><br /><a href="rules-g.html#g0103">G0103</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0055">C0055</a><br /><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>--- Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0165">G0165</a><br /><a href="rules-r.html#r0106">R0106</a><br /><a href="rules-r.html#r0448">R0448</a></td>
</tr><tr>
    <td><strong>--- SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0569">C0569</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0107">R0107</a></td>
</tr><tr>
    <td><strong>--- GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0670">C0670</a><br /><a href="rules-g.html#g0670">G0670</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-g.html#g0006">G0006</a></td>
</tr><tr>
    <td><strong>-- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0339">C0339</a><br /><a href="rules-r.html#r0855">R0855</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-r.html#r0472">R0472</a><br /><a href="rules-r.html#r0474">R0474</a><br /><a href="rules-r.html#r0476">R0476</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0473">R0473</a></td>
</tr><tr>
    <td>--- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentType.zip">CL214</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r0020">R0020</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>--- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>--- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>-- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>-- ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r3060">R3060</a></td>
</tr><tr>
    <td>--- Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- INCIDENT</strong></td>
    <td>O</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0015">G0015</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Code</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_IncidentCode.zip">CL019</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Text</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- ENDORSEMENT</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>---- Authority</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Place</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- LOCATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_QualifierOfIdentificationIncident.zip">CL038</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td><a href="rules-c.html#c0460">C0460</a></td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0460">C0460</a></td>
</tr><tr>
    <td>----- Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0014">G0014</a></td>
</tr><tr>
    <td>----- Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0014">G0014</a></td>
</tr><tr>
    <td><strong>---- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0460">C0460</a></td>
</tr><tr>
    <td>----- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>----- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-s.html#s1023">S1023</a><br /><a href="rules-c.html#c0040">C0040</a><br /><a href="rules-c.html#c0240">C0240</a><br /><a href="rules-g.html#g0103">G0103</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0820">C0820</a><br /><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0016">G0016</a></td>
</tr><tr>
    <td>---- Number of seals</td>
    <td>D</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0396">C0396</a><br /><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0023">G0023</a><br /><a href="rules-r.html#r0106">R0106</a><br /><a href="rules-r.html#r0448">R0448</a></td>
</tr><tr>
    <td><strong>---- SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0569">C0569</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0107">R0107</a></td>
</tr><tr>
    <td><strong>---- GOODS REFERENCE</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0670">G0670</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-g.html#g0006">G0006</a></td>
</tr><tr>
    <td><strong>--- TRANSHIPMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0240">C0240</a></td>
</tr><tr>
    <td>---- Container indicator</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-g.html#g0029">G0029</a></td>
</tr><tr>
    <td><strong>---- TRANSPORT MEANS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-g.html#g0023">G0023</a></td>
</tr><tr>
    <td>----- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0023">G0023</a></td>
</tr><tr>
    <td>----- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-g.html#g0023">G0023</a></td>
</tr><tr>
    <td><strong>-- HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>--- Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0983">R0983</a></td>
</tr><tr>
    <td>--- Security indicator from export declaration</td>
    <td>O</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeSecurity.zip">CL217</a></td>
    <td><a href="rules-g.html#g0025">G0025</a><br /><a href="rules-g.html#g0026">G0026</a></td>
</tr><tr>
    <td><strong>--- CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0349">C0349</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td><strong>---- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>----- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>----- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0001">C0001</a><br /><a href="rules-g.html#g0001">G0001</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0851">R0851</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td><strong>---- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>----- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>----- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0339">C0339</a><br /><a href="rules-r.html#r0855">R0855</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-r.html#r0472">R0472</a><br /><a href="rules-r.html#r0474">R0474</a><br /><a href="rules-r.html#r0476">R0476</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0473">R0473</a></td>
</tr><tr>
    <td>---- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0026">G0026</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL228</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0416">R0416</a></td>
</tr><tr>
    <td>---- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>---- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>--- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>--- ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>---- Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r3062">R3062</a></td>
</tr><tr>
    <td>---- Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- CONSIGNMENT ITEM</strong></td>
    <td>R</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0988">R0988</a></td>
</tr><tr>
    <td>---- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-r.html#r0007">R0007</a></td>
</tr><tr>
    <td>---- Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeItemLevel.zip">CL232</a></td>
    <td><a href="rules-c.html#c0045">C0045</a><br /><a href="rules-r.html#r0601">R0601</a><br /><a href="rules-r.html#r0909">R0909</a></td>
</tr><tr>
    <td>---- Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0343">C0343</a></td>
</tr><tr>
    <td><strong>---- CONSIGNEE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0001">G0001</a><br /><a href="rules-g.html#g0989">G0989</a></td>
</tr><tr>
    <td>----- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0851">R0851</a></td>
</tr><tr>
    <td>----- Name</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>----- ADDRESS</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0989">G0989</a></td>
</tr><tr>
    <td>------ Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>------ Postcode</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>------ City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>------ Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CUSCode.zip">CL016</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>----- COMMODITY CODE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0153">C0153</a></td>
</tr><tr>
    <td>------ Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_HScode.zip">CL152</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>------ Combined nomenclature code</td>
    <td>O</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0060">R0060</a></td>
</tr><tr>
    <td><strong>----- DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0300">G0300</a></td>
</tr><tr>
    <td>------ Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>------ UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnDangerousGoodsCode.zip">CL101</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>----- GOODS MEASURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>------ Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-r.html#r0221">R0221</a></td>
</tr><tr>
    <td>------ Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0837">C0837</a><br /><a href="rules-r.html#r0223">R0223</a></td>
</tr><tr>
    <td><strong>---- PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip">CL017</a></td>
    <td><a href="rules-r.html#r0220">R0220</a></td>
</tr><tr>
    <td>----- Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0060">C0060</a><br /><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-r.html#r0219">R0219</a><br /><a href="rules-r.html#r0364">R0364</a></td>
</tr><tr>
    <td>----- Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0060">C0060</a><br /><a href="rules-g.html#g0024">G0024</a></td>
</tr><tr>
    <td><strong>---- PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentType.zip">CL214</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r0020">R0020</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>----- Goods item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>----- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a><br /><a href="rules-g.html#g0989">G0989</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>---- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0015">C0015</a><br /><a href="rules-g.html#g0050">G0050</a><br /><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-r.html#r0023">R0023</a></td>
</tr><tr>
    <td><strong>---- ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>----- Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r3061">R3061</a></td>
</tr><tr>
    <td>----- Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>