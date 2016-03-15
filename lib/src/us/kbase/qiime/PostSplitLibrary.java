
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
 * <p>Original spec-file type: PostSplitLibrary</p>
 * <pre>
 * Handle to a FASTA file in the QIIME post-split library file format.
 * see http://qiime.org/documentation/file_formats.html#post-split-libraries-fasta-file-overview
 * @metadata ws fasta.file_name as Filename
 * @metadata ws fasta.size as File Size
 * @metadata ws fasta.remote_md5 as File MD5
 * @metadata ws fasta.remote_sha1 as File SHA1
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "fasta"
})
public class PostSplitLibrary {

    /**
     * <p>Original spec-file type: FastaHandle</p>
     * <pre>
     * @optional remote_md5
     * @optional remote_sha1
     * </pre>
     * 
     */
    @JsonProperty("fasta")
    private FastaHandle fasta;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    /**
     * <p>Original spec-file type: FastaHandle</p>
     * <pre>
     * @optional remote_md5
     * @optional remote_sha1
     * </pre>
     * 
     */
    @JsonProperty("fasta")
    public FastaHandle getFasta() {
        return fasta;
    }

    /**
     * <p>Original spec-file type: FastaHandle</p>
     * <pre>
     * @optional remote_md5
     * @optional remote_sha1
     * </pre>
     * 
     */
    @JsonProperty("fasta")
    public void setFasta(FastaHandle fasta) {
        this.fasta = fasta;
    }

    public PostSplitLibrary withFasta(FastaHandle fasta) {
        this.fasta = fasta;
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
        return ((((("PostSplitLibrary"+" [fasta=")+ fasta)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
