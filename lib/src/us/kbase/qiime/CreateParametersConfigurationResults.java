
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
 * <p>Original spec-file type: CreateParametersConfigurationResults</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report_name",
    "report_ref",
    "parameters_configuration_ref"
})
public class CreateParametersConfigurationResults {

    @JsonProperty("report_name")
    private String reportName;
    @JsonProperty("report_ref")
    private String reportRef;
    @JsonProperty("parameters_configuration_ref")
    private String parametersConfigurationRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report_name")
    public String getReportName() {
        return reportName;
    }

    @JsonProperty("report_name")
    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public CreateParametersConfigurationResults withReportName(String reportName) {
        this.reportName = reportName;
        return this;
    }

    @JsonProperty("report_ref")
    public String getReportRef() {
        return reportRef;
    }

    @JsonProperty("report_ref")
    public void setReportRef(String reportRef) {
        this.reportRef = reportRef;
    }

    public CreateParametersConfigurationResults withReportRef(String reportRef) {
        this.reportRef = reportRef;
        return this;
    }

    @JsonProperty("parameters_configuration_ref")
    public String getParametersConfigurationRef() {
        return parametersConfigurationRef;
    }

    @JsonProperty("parameters_configuration_ref")
    public void setParametersConfigurationRef(String parametersConfigurationRef) {
        this.parametersConfigurationRef = parametersConfigurationRef;
    }

    public CreateParametersConfigurationResults withParametersConfigurationRef(String parametersConfigurationRef) {
        this.parametersConfigurationRef = parametersConfigurationRef;
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
        return ((((((((("CreateParametersConfigurationResults"+" [reportName=")+ reportName)+", reportRef=")+ reportRef)+", parametersConfigurationRef=")+ parametersConfigurationRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
