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
    <td>-- MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>-- Incident notification date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
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
    <td><strong>- CUSTOMS OFFICE OF INCIDENT REGISTRATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/COL-Generic-20230601.zip">CL141</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- INCIDENT</strong></td>
    <td>R</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
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
    <td><a href="rules-g.html">G0002</a></td>
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
    <td><a href="rules-c.html">C0460</a></td>
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
    <td><a href="rules-c.html">C0460</a></td>
</tr><tr>
    <td>----- Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0014</a></td>
</tr><tr>
    <td>----- Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0014</a></td>
</tr><tr>
    <td><strong>---- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0460</a></td>
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
    <td><a href="rules-c.html">C0505</a></td>
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
    <td><a href="rules-s.html">S1023</a><br /><a href="rules-c.html">C0040</a><br /><a href="rules-c.html">C0240</a><br /><a href="rules-g.html">G0103</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0820</a><br /><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0016</a></td>
</tr><tr>
    <td>---- Number of seals</td>
    <td>D</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0396</a><br /><a href="rules-g.html">G0021</a><br /><a href="rules-g.html">G0023</a><br /><a href="rules-r.html">R0106</a><br /><a href="rules-r.html">R0448</a></td>
</tr><tr>
    <td><strong>---- SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0569</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0023</a><br /><a href="rules-r.html">R0107</a></td>
</tr><tr>
    <td><strong>---- GOODS REFERENCE</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0670</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0005</a><br /><a href="rules-g.html">G0006</a></td>
</tr><tr>
    <td><strong>--- TRANSHIPMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0240</a></td>
</tr><tr>
    <td>---- Container indicator</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-g.html">G0029</a></td>
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
    <td><a href="rules-g.html">G0023</a></td>
</tr><tr>
    <td>----- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0023</a></td>
</tr><tr>
    <td>----- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-g.html">G0023</a></td>
</tr></table>