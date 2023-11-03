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
    <td>D</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0685</a></td>
</tr><tr>
    <td>-- MRN</td>
    <td>D</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0685</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>-- Control notification date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>-- Notification type</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_NotificationType.zip">CL384</a></td>
    <td>&nbsp;</td>
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
    <td><strong>- TYPE OF CONTROLS</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0452</a></td>
</tr><tr>
    <td>-- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>-- Type</td>
    <td>R</td>
    <td>an..3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_ControlType.zip">CL716</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Text</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0451</a></td>
</tr><tr>
    <td><strong>- REQUESTED DOCUMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0455</a></td>
</tr><tr>
    <td>-- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>-- Document type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RequestedDocumentType.zip">CL215</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Description</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>