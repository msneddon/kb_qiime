/*


*/
module QIIME {



    /* @id handle */
    typedef string handle_id;

    /*
        @optional remote_md5
        @optional remote_sha1
    */
    typedef structure {
        handle_id hid;
        string file_name;
        string id;
        string url;
        string remote_md5;
        string remote_sha1;
        int size;
    } FastaHandle;


    /*
        Handle to a FASTA file in the QIIME post-split library file format.
        see http://qiime.org/documentation/file_formats.html#post-split-libraries-fasta-file-overview

        @metadata ws fasta.file_name as Filename
        @metadata ws fasta.size as File Size
        @metadata ws fasta.remote_md5 as File MD5
        @metadata ws fasta.remote_sha1 as File SHA1
    */
    typedef structure {
        FastaHandle fasta;
    } PostSplitLibrary;



    /*
        @optional remote_md5
        @optional remote_sha1
    */
    typedef structure {
        handle_id hid;
        string file_name;
        string id;
        string url;
        string remote_md5;
        string remote_sha1;
        int size;
    } BIOMHandle;

    /*
        @metadata ws length(lines) as N Lines
    */
    typedef structure {
        list<string> lines;
    } QIIMEParametersFile;


    /* OTU Table, generally a wrapper of a BIOM file */
    typedef structure {
        BIOMHandle biom;

        int n_samples;
        int n_observations;
        int count;
        float density;

        mapping<string,float> sample_detail;

        string summary;
    } OTUTable;


    typedef structure {
        string workspace;
        string post_split_lib;
        string otu_table_name;
        string parameters_file;
    } PickClosedRefOTUsParams;

    typedef structure {
        string otu_table_ref;
        string report_name;
        string report_ref;
    } PickClosedRefOTUsResults;

    funcdef pick_closed_reference_otus(PickClosedRefOTUsParams params)
                returns(PickClosedRefOTUsResults) authentication required;

};