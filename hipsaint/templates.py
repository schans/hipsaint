"""
Templates used to build hipchat api payloads
"""

host_template = """
<strong>{timestamp} - {hostname}  (nagios@{nagios_host})</strong><br/>
<strong>Type:</strong> {ntype}<br/>
<strong>Host:</strong> {hostname} (<a href="{hostaddress}">{hostaddress}</a>)<br/>
<strong>State:</strong> {state}<br>
<strong>Info:</strong>
<pre>{hostoutput}</pre>
"""

host_short_template = """[{ntype}] <strong>{hostname}</strong>: {hostoutput}"""

host_ack_template = """
<strong>{timestamp} - {hostname}  (nagios@{nagios_host})</strong><br/>
<strong>Type:</strong> {ntype}<br/>
<strong>Host:</strong> {hostname} (<a href="{hostaddress}">{hostaddress}</a>)<br/>
<strong>State:</strong> {state}<br>
<strong>Author:</strong> {author}<br/>
<strong>Message:</strong> {message}<br/>
<strong>Info:</strong>
<pre>{hostoutput}</pre>
"""

host_ack_short_template = """[{ntype}] <strong>{hostname}</strong>: {hostoutput} by <strong>{author}</strong>: {message}"""

service_template = """
<strong>{timestamp} - {servicedesc} on {hostalias} (nagios@{nagios_host})</strong><br/>
<strong>Type:</strong> {ntype}<br/>
<strong>Host:</strong> {hostalias} (<a href="{hostaddress}">{hostaddress}</a>)<br/>
<strong>State:</strong> {state}<br/>
<strong>Info:</strong>
<pre>{serviceoutput}</pre>
"""

service_short_template = """[{ntype}] <strong>{hostalias}</strong> {servicedesc}: {serviceoutput}"""

service_ack_template = """
<strong>{timestamp} - {servicedesc} on {hostalias} (nagios@{nagios_host})</strong><br/>
<strong>Type:</strong> {ntype}<br/>
<strong>Host:</strong> {hostalias} (<a href="{hostaddress}">{hostaddress}</a>)<br/>
<strong>State:</strong> {state}<br/>
<strong>Author:</strong> {author}<br/>
<strong>Message:</strong> {message}<br/>
<strong>Info:</strong>
<pre>{serviceoutput}</pre>
"""

service_ack_short_template = """[{ntype}] <strong>{hostalias}</strong> {servicedesc}: {serviceoutput} by <strong>{author}</strong>: {message}"""


templates = {'host': host_template, 'short-host': host_short_template,
             'host-ack': host_ack_template, 'short-host-ack': host_ack_short_template,
             'service': service_template, 'short-service': service_short_template,
             'service-ack': service_ack_template, 'short-service-ack': service_ack_short_template}
