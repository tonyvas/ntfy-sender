# ntfy-sender
Wrapper for ntfy.sh notification tool

## Usage
<pre>
    <b>python3 send.py</b> --topic="<i>...</i>" [ --server="<i>...</i>" --title="<i>...</i>" --message="<i>...</i>" --priority=<i>...</i> --tag="<i>...</i>" --tag="<i>...</i>" ]
</pre>

<pre>
<b>python3 send.py</b>
The script to run

<b>topic</b>: string, <u>required</u>
The topic (channel/id) to send your notification to

<b>server</b>: URL string
The server ntfy is hosted on if self-hosted. Optional, default is https://ntfy.sh

<b>title</b>: string
The title of your notification

<b>message</b>: string
The main content of notification

<b>priority</b>: integer
The priority level
    <b>1</b>: Min priority
    <b>2</b>: Low priority
    <b>3</b>: Default priority
    <b>4</b>: High priority
    <b>5</b>: Max priority

<b>tag</b>: string
Custom tags, can be repeated for multiple tags
</pre>