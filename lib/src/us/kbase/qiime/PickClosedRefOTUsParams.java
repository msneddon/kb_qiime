
package us.kbase.qiime;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: PickClosedRefOTUsParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace",
    "post_split_lib",
    "otu_table_name",
    "parameters_config",
    "rev_strand_match"
})
public class PickClosedRefOTUsParams {

    @JsonProperty("workspace")
    private String workspace;
    @JsonProperty("post_split_lib")
    private String postSplitLib;
    @JsonProperty("otu_table_name")
    private String otuTableName;
    @JsonProperty("parameters_config")
    private String parametersConfig;
    @JsonProperty("rev_strand_match")
    private Long revStrandMatch;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace")
    public String getWorkspace() {
        return workspace;
    }

    @JsonProperty("workspace")
    public void setWorkspace(String workspace) {
        this.workspace = workspace;
    }

    public PickClosedRefOTUsParams withWorkspace(String workspace) {
        this.workspace = workspace;
        return this;
    }

    @JsonProperty("post_split_lib")
    public String getPostSplitLib() {
        return postSplitLib;
    }

    @JsonProperty("post_split_lib")
    public void setPostSplitLib(String postSplitLib) {
        this.postSplitLib = postSplitLib;
    }

    public PickClosedRefOTUsParams withPostSplitLib(String postSplitLib) {
        this.postSplitLib = postSplitLib;
        return this;
    }

    @JsonProperty("otu_table_name")
    public String getOtuTableName() {
        return otuTableName;
    }

    @JsonProperty("otu_table_name")
    public void setOtuTableName(String otuTableName) {
        this.otuTableName = otuTableName;
    }

    public PickClosedRefOTUsParams withOtuTableName(String otuTableName) {
        this.otuTableName = otuTableName;
        return this;
    }

    @JsonProperty("parameters_config")
    public String getParametersConfig() {
        return parametersConfig;
    }

    @JsonProperty("parameters_config")
    public void setParametersConfig(String parametersConfig) {
        this.parametersConfig = parametersConfig;
    }

    public PickClosedRefOTUsParams withParametersConfig(String parametersConfig) {
        this.parametersConfig = parametersConfig;
        return this;
    }

    @JsonProperty("rev_strand_match")
    public Long getRevStrandMatch() {
        return revStrandMatch;
    }

    @JsonProperty("rev_strand_match")
    public void setRevStrandMatch(Long revStrandMatch) {
        this.revStrandMatch = revStrandMatch;
    }

    public PickClosedRefOTUsParams withRevStrandMatch(Long revStrandMatch) {
        this.revStrandMatch = revStrandMatch;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((("PickClosedRefOTUsParams"+" [workspace=")+ workspace)+", postSplitLib=")+ postSplitLib)+", otuTableName=")+ otuTableName)+", parametersConfig=")+ parametersConfig)+", revStrandMatch=")+ revStrandMatch)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
