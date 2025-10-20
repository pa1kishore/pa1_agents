
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


#### Option-2 Deploying Ask Agents on cloud run
<pre>
adk deploy agent_engine \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--staging_bucket=gs://pa1_adk_agents \
--display_name=ask-agent \
ask_agent
</pre>


### Option-3 Deploying Ask Agents on cloud run using custom docker file
<pre>
gcloud run deploy ask-agent \
--source=temp_staging \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION 
</pre>