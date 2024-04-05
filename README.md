# ntfy-sender
Wrapper for ntfy.sh notification tool

## Usage
<pre>
    <b>python3 send.py</b> <u>topic="<i>...</i>"</u> [ <u>title="<i>...</i>"</u> <u>message="<i>...</i>"</u> <u>priority=<i>...</i></u> <u>tag="<i>...</i>"</u> <u>tag="<i>...</i>"</u> ]
</pre>

<pre>
<b>python3 send.py</b>
The script to run

<b>topic</b>: string, <u>required</u>
The topic (channel/id) to send your notification to

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

<b>tag</b>: string(s)
Custom tags, can be repeated for multiple tags
</pre>