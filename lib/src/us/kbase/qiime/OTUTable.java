
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
 * <p>Original spec-file type: OTUTable</p>
 * <pre>
 * OTU Table, generally a wrapper of a BIOM file 
 *         TODO: add:
 *             int n_samples;
 *             int n_observations;
 *             int count;
 *             float density;
 *             mapping<string,float> sample_detail;
 *         @metadata ws summary as Summary
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "biom",
    "summary"
})
public class OTUTable {

    /**
     * <p>Original spec-file type: BIOMHandle</p>
     * <pre>
     * @optional remote_md5
     * @optional remote_sha1
     * </pre>
     * 
     */
    @JsonProperty("biom")
    private BIOMHandle biom;
    @JsonProperty("summary")
    private String summary;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    /**
     * <p>Original spec-file type: BIOMHandle</p>
     * <pre>
     * @optional remote_md5
     * @optional remote_sha1
     * </pre>
     * 
     */
    @JsonProperty("biom")
    public BIOMHandle getBiom() {
        return biom;
    }

    /**
     * <p>Original spec-file type: BIOMHandle</p>
     * <pre>
     * @optional remote_md5
     * @optional remote_sha1
     * </pre>
     * 
     */
    @JsonProperty("biom")
    public void setBiom(BIOMHandle biom) {
        this.biom = biom;
    }

    public OTUTable withBiom(BIOMHandle biom) {
        this.biom = biom;
        return this;
    }

    @JsonProperty("summary")
    public String getSummary() {
        return summary;
    }

    @JsonProperty("summary")
    public void setSummary(String summary) {
        this.summary = summary;
    }

    public OTUTable withSummary(String summary) {
        this.summary = summary;
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
        return ((((((("OTUTable"+" [biom=")+ biom)+", summary=")+ summary)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
