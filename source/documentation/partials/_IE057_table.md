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
    <td>-&nbsp; Message sender</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message recipient</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp; Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message type</td>
    <td>R</td>
    <td>an6</td>
    <td>CL060</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0511">C0511</a><br /><a href="rules-r.html#r0008">R0008</a></td>
</tr><tr>
    <td><strong>-&nbsp; TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Business rejection type</td>
    <td>R</td>
    <td>an3</td>
    <td>CL570</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Rejection date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Rejection code</td>
    <td>R</td>
    <td>n..2</td>
    <td>CL227</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Rejection reason</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0492">C0492</a></td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0868">G0868</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td><strong>-&nbsp; FUNCTIONAL ERROR</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0217">G0217</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Error pointer</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0009">G0009</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Error code</td>
    <td>R</td>
    <td>n2</td>
    <td>CL180</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Error reason</td>
    <td>R</td>
    <td>an..7</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0010">G0010</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Original attribute value</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>