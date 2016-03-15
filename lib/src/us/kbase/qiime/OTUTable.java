
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
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "biom",
    "n_samples",
    "n_observations",
    "count",
    "density",
    "sample_detail",
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
    @JsonProperty("n_samples")
    private Long nSamples;
    @JsonProperty("n_observations")
    private Long nObservations;
    @JsonProperty("count")
    private Long count;
    @JsonProperty("density")
    private java.lang.Double density;
    @JsonProperty("sample_detail")
    private Map<String, Double> sampleDetail;
    @JsonProperty("summary")
    private java.lang.String summary;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

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

    @JsonProperty("n_samples")
    public Long getNSamples() {
        return nSamples;
    }

    @JsonProperty("n_samples")
    public void setNSamples(Long nSamples) {
        this.nSamples = nSamples;
    }

    public OTUTable withNSamples(Long nSamples) {
        this.nSamples = nSamples;
        return this;
    }

    @JsonProperty("n_observations")
    public Long getNObservations() {
        return nObservations;
    }

    @JsonProperty("n_observations")
    public void setNObservations(Long nObservations) {
        this.nObservations = nObservations;
    }

    public OTUTable withNObservations(Long nObservations) {
        this.nObservations = nObservations;
        return this;
    }

    @JsonProperty("count")
    public Long getCount() {
        return count;
    }

    @JsonProperty("count")
    public void setCount(Long count) {
        this.count = count;
    }

    public OTUTable withCount(Long count) {
        this.count = count;
        return this;
    }

    @JsonProperty("density")
    public java.lang.Double getDensity() {
        return density;
    }

    @JsonProperty("density")
    public void setDensity(java.lang.Double density) {
        this.density = density;
    }

    public OTUTable withDensity(java.lang.Double density) {
        this.density = density;
        return this;
    }

    @JsonProperty("sample_detail")
    public Map<String, Double> getSampleDetail() {
        return sampleDetail;
    }

    @JsonProperty("sample_detail")
    public void setSampleDetail(Map<String, Double> sampleDetail) {
        this.sampleDetail = sampleDetail;
    }

    public OTUTable withSampleDetail(Map<String, Double> sampleDetail) {
        this.sampleDetail = sampleDetail;
        return this;
    }

    @JsonProperty("summary")
    public java.lang.String getSummary() {
        return summary;
    }

    @JsonProperty("summary")
    public void setSummary(java.lang.String summary) {
        this.summary = summary;
    }

    public OTUTable withSummary(java.lang.String summary) {
        this.summary = summary;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((((((((("OTUTable"+" [biom=")+ biom)+", nSamples=")+ nSamples)+", nObservations=")+ nObservations)+", count=")+ count)+", density=")+ density)+", sampleDetail=")+ sampleDetail)+", summary=")+ summary)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
