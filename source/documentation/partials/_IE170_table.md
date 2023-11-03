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
    <td><a href="rules-g.html">G0002</a></td>
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
    <td><a href="rules-c.html">C0511</a><br /><a href="rules-r.html">R0008</a></td>
</tr><tr>
    <td><strong>- TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- LRN</td>
    <td>R</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Limit date</td>
    <td>D</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0840</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>- CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDeparture.zip">CL171</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0120</a><br /><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td>-- TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0904</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>-- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td><strong>-- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
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
    <td><a href="rules-c.html">C0505</a></td>
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
    <td><strong>- REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0850</a></td>
</tr><tr>
    <td>-- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td>-- Status</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RepresentativeStatusCode.zip">CL094</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>--- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>- CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0045</a></td>
</tr><tr>
    <td>-- Container indicator</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-c.html">C0824</a><br /><a href="rules-g.html">G0332</a></td>
</tr><tr>
    <td>-- Inland mode of transport</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip">CL218</a></td>
    <td><a href="rules-c.html">C0170</a></td>
</tr><tr>
    <td>-- Mode of transport at the border</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip">CL218</a></td>
    <td><a href="rules-c.html">C0600</a><br /><a href="rules-g.html">G0020</a><br /><a href="rules-g.html">G0115</a></td>
</tr><tr>
    <td><strong>-- TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0823</a><br /><a href="rules-g.html">G0103</a><br /><a href="rules-g.html">G0196</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0055</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>--- Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0021</a><br /><a href="rules-g.html">G0165</a><br /><a href="rules-r.html">R0106</a><br /><a href="rules-r.html">R0448</a></td>
</tr><tr>
    <td><strong>--- SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0569</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0107</a></td>
</tr><tr>
    <td><strong>--- GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0670</a><br /><a href="rules-g.html">G0670</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0005</a><br /><a href="rules-g.html">G0006</a></td>
</tr><tr>
    <td><strong>-- LOCATION OF GOODS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Type of location</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfLocation.zip">CL347</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_QualifierOfTheIdentification.zip">CL326</a></td>
    <td><a href="rules-g.html">G0500</a></td>
</tr><tr>
    <td>--- Authorisation number</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>--- Additional identifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0671</a></td>
</tr><tr>
    <td>--- UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td><strong>--- CUSTOMS OFFICE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDeparture.zip">CL171</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0014</a></td>
</tr><tr>
    <td>---- Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0014</a></td>
</tr><tr>
    <td><strong>--- ECONOMIC OPERATOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td><strong>--- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
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
    <td><a href="rules-c.html">C0505</a></td>
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
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- POSTCODE ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- House number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0382</a></td>
</tr><tr>
    <td>---- Postcode</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryAddressPostcodeBased.zip">CL190</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- CONTACT PERSON</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a><br /><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>-- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0833</a><br /><a href="rules-g.html">G0088</a><br /><a href="rules-g.html">G0119</a><br /><a href="rules-g.html">G0196</a><br /><a href="rules-r.html">R0855</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-b.html">B1091</a><br /><a href="rules-r.html">R0472</a><br /><a href="rules-r.html">R0474</a><br /><a href="rules-r.html">R0476</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0473</a></td>
</tr><tr>
    <td>--- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- ACTIVE BORDER TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0807</a><br /><a href="rules-r.html">R0790</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Customs office at border reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/COL-Generic-20230601.zip">CL141</a></td>
    <td><a href="rules-g.html">G0789</a></td>
</tr><tr>
    <td>--- Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationofMeansOfTransportActive.zip">CL219</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0076</a></td>
</tr><tr>
    <td>--- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Conveyance reference number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0808</a><br /><a href="rules-g.html">G0002</a><br /><a href="rules-r.html">R0315</a></td>
</tr><tr>
    <td><strong>-- PLACE OF LOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0404</a></td>
</tr><tr>
    <td>--- UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Country</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0387</a></td>
</tr><tr>
    <td>--- Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0387</a></td>
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
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td><strong>--- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0833</a><br /><a href="rules-g.html">G0088</a><br /><a href="rules-g.html">G0119</a><br /><a href="rules-g.html">G0196</a><br /><a href="rules-r.html">R0506</a><br /><a href="rules-r.html">R0855</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-r.html">R0472</a><br /><a href="rules-r.html">R0474</a><br /><a href="rules-r.html">R0476</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0473</a></td>
</tr><tr>
    <td>---- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td>&nbsp;</td>
</tr></table>