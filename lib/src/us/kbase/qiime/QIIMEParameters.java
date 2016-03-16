
package us.kbase.qiime;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: QIIMEParameters</p>
 * <pre>
 * @metadata ws length(lines) as N Lines
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "lines"
})
public class QIIMEParameters {

    @JsonProperty("lines")
    private List<String> lines;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("lines")
    public List<String> getLines() {
        return lines;
    }

    @JsonProperty("lines")
    public void setLines(List<String> lines) {
        this.lines = lines;
    }

    public QIIMEParameters withLines(List<String> lines) {
        this.lines = lines;
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
        return ((((("QIIMEParameters"+" [lines=")+ lines)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
