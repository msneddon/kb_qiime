
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
 * <p>Original spec-file type: BIOMHandle</p>
 * <pre>
 * @optional remote_md5
 * @optional remote_sha1
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "hid",
    "file_name",
    "id",
    "url",
    "remote_md5",
    "remote_sha1",
    "size"
})
public class BIOMHandle {

    @JsonProperty("hid")
    private String hid;
    @JsonProperty("file_name")
    private String fileName;
    @JsonProperty("id")
    private String id;
    @JsonProperty("url")
    private String url;
    @JsonProperty("remote_md5")
    private String remoteMd5;
    @JsonProperty("remote_sha1")
    private String remoteSha1;
    @JsonProperty("size")
    private Long size;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("hid")
    public String getHid() {
        return hid;
    }

    @JsonProperty("hid")
    public void setHid(String hid) {
        this.hid = hid;
    }

    public BIOMHandle withHid(String hid) {
        this.hid = hid;
        return this;
    }

    @JsonProperty("file_name")
    public String getFileName() {
        return fileName;
    }

    @JsonProperty("file_name")
    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public BIOMHandle withFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    public BIOMHandle withId(String id) {
        this.id = id;
        return this;
    }

    @JsonProperty("url")
    public String getUrl() {
        return url;
    }

    @JsonProperty("url")
    public void setUrl(String url) {
        this.url = url;
    }

    public BIOMHandle withUrl(String url) {
        this.url = url;
        return this;
    }

    @JsonProperty("remote_md5")
    public String getRemoteMd5() {
        return remoteMd5;
    }

    @JsonProperty("remote_md5")
    public void setRemoteMd5(String remoteMd5) {
        this.remoteMd5 = remoteMd5;
    }

    public BIOMHandle withRemoteMd5(String remoteMd5) {
        this.remoteMd5 = remoteMd5;
        return this;
    }

    @JsonProperty("remote_sha1")
    public String getRemoteSha1() {
        return remoteSha1;
    }

    @JsonProperty("remote_sha1")
    public void setRemoteSha1(String remoteSha1) {
        this.remoteSha1 = remoteSha1;
    }

    public BIOMHandle withRemoteSha1(String remoteSha1) {
        this.remoteSha1 = remoteSha1;
        return this;
    }

    @JsonProperty("size")
    public Long getSize() {
        return size;
    }

    @JsonProperty("size")
    public void setSize(Long size) {
        this.size = size;
    }

    public BIOMHandle withSize(Long size) {
        this.size = size;
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
        return ((((((((((((((((("BIOMHandle"+" [hid=")+ hid)+", fileName=")+ fileName)+", id=")+ id)+", url=")+ url)+", remoteMd5=")+ remoteMd5)+", remoteSha1=")+ remoteSha1)+", size=")+ size)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
