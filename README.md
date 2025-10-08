
#### Setting Gloud to path
<pre>
export PATH="$PATH:/Users/pa1/Downloads/google-cloud-sdk/bin"
</pre>
#### Option-1 Deploying Ask Agents on cloud run
<pre>
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=ask-agent \
--app_name=ask-agent \
--with_ui \
ask_agent
</pre>

