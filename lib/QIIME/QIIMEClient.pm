package QIIME::QIIMEClient;

use JSON::RPC::Client;
use POSIX;
use strict;
use Data::Dumper;
use URI;
use Bio::KBase::Exceptions;
my $get_time = sub { time, 0 };
eval {
    require Time::HiRes;
    $get_time = sub { Time::HiRes::gettimeofday() };
};

use Bio::KBase::AuthToken;

# Client version should match Impl version
# This is a Semantic Version number,
# http://semver.org
our $VERSION = "0.1.0";

=head1 NAME

QIIME::QIIMEClient

=head1 DESCRIPTION





=cut

sub new
{
    my($class, $url, @args) = @_;
    

    my $self = {
	client => QIIME::QIIMEClient::RpcClient->new,
	url => $url,
	headers => [],
    };

    chomp($self->{hostname} = `hostname`);
    $self->{hostname} ||= 'unknown-host';

    #
    # Set up for propagating KBRPC_TAG and KBRPC_METADATA environment variables through
    # to invoked services. If these values are not set, we create a new tag
    # and a metadata field with basic information about the invoking script.
    #
    if ($ENV{KBRPC_TAG})
    {
	$self->{kbrpc_tag} = $ENV{KBRPC_TAG};
    }
    else
    {
	my ($t, $us) = &$get_time();
	$us = sprintf("%06d", $us);
	my $ts = strftime("%Y-%m-%dT%H:%M:%S.${us}Z", gmtime $t);
	$self->{kbrpc_tag} = "C:$0:$self->{hostname}:$$:$ts";
    }
    push(@{$self->{headers}}, 'Kbrpc-Tag', $self->{kbrpc_tag});

    if ($ENV{KBRPC_METADATA})
    {
	$self->{kbrpc_metadata} = $ENV{KBRPC_METADATA};
	push(@{$self->{headers}}, 'Kbrpc-Metadata', $self->{kbrpc_metadata});
    }

    if ($ENV{KBRPC_ERROR_DEST})
    {
	$self->{kbrpc_error_dest} = $ENV{KBRPC_ERROR_DEST};
	push(@{$self->{headers}}, 'Kbrpc-Errordest', $self->{kbrpc_error_dest});
    }

    #
    # This module requires authentication.
    #
    # We create an auth token, passing through the arguments that we were (hopefully) given.

    {
	my $token = Bio::KBase::AuthToken->new(@args);
	
	if (!$token->error_message)
	{
	    $self->{token} = $token->token;
	    $self->{client}->{token} = $token->token;
	}
        else
        {
	    #
	    # All methods in this module require authentication. In this case, if we
	    # don't have a token, we can't continue.
	    #
	    die "Authentication failed: " . $token->error_message;
	}
    }

    my $ua = $self->{client}->ua;	 
    my $timeout = $ENV{CDMI_TIMEOUT} || (30 * 60);	 
    $ua->timeout($timeout);
    bless $self, $class;
    #    $self->_validate_version();
    return $self;
}




=head2 pick_closed_reference_otus

  $return = $obj->pick_closed_reference_otus($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a QIIME.PickClosedRefOTUsParams
$return is a QIIME.PickClosedRefOTUsResults
PickClosedRefOTUsParams is a reference to a hash where the following keys are defined:
	workspace has a value which is a string
	post_split_lib has a value which is a string
	otu_table_name has a value which is a string
	parameters_config has a value which is a string
	rev_strand_match has a value which is an int
PickClosedRefOTUsResults is a reference to a hash where the following keys are defined:
	otu_table_ref has a value which is a string
	report_name has a value which is a string
	report_ref has a value which is a string

</pre>

=end html

=begin text

$params is a QIIME.PickClosedRefOTUsParams
$return is a QIIME.PickClosedRefOTUsResults
PickClosedRefOTUsParams is a reference to a hash where the following keys are defined:
	workspace has a value which is a string
	post_split_lib has a value which is a string
	otu_table_name has a value which is a string
	parameters_config has a value which is a string
	rev_strand_match has a value which is an int
PickClosedRefOTUsResults is a reference to a hash where the following keys are defined:
	otu_table_ref has a value which is a string
	report_name has a value which is a string
	report_ref has a value which is a string


=end text

=item Description



=back

=cut

 sub pick_closed_reference_otus
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function pick_closed_reference_otus (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to pick_closed_reference_otus:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'pick_closed_reference_otus');
	}
    }

    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
	method => "QIIME.pick_closed_reference_otus",
	params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'pick_closed_reference_otus',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method pick_closed_reference_otus",
					    status_line => $self->{client}->status_line,
					    method_name => 'pick_closed_reference_otus',
				       );
    }
}
 


=head2 create_parameters_configuration

  $return = $obj->create_parameters_configuration($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a QIIME.CreateParametersConfigurationParams
$return is a QIIME.CreateParametersConfigurationResults
CreateParametersConfigurationParams is a reference to a hash where the following keys are defined:
	workspace has a value which is a string
	name has a value which is a string
	content has a value which is a string
CreateParametersConfigurationResults is a reference to a hash where the following keys are defined:
	report_name has a value which is a string
	report_ref has a value which is a string
	parameters_configuration_ref has a value which is a string

</pre>

=end html

=begin text

$params is a QIIME.CreateParametersConfigurationParams
$return is a QIIME.CreateParametersConfigurationResults
CreateParametersConfigurationParams is a reference to a hash where the following keys are defined:
	workspace has a value which is a string
	name has a value which is a string
	content has a value which is a string
CreateParametersConfigurationResults is a reference to a hash where the following keys are defined:
	report_name has a value which is a string
	report_ref has a value which is a string
	parameters_configuration_ref has a value which is a string


=end text

=item Description



=back

=cut

 sub create_parameters_configuration
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function create_parameters_configuration (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to create_parameters_configuration:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'create_parameters_configuration');
	}
    }

    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
	method => "QIIME.create_parameters_configuration",
	params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'create_parameters_configuration',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method create_parameters_configuration",
					    status_line => $self->{client}->status_line,
					    method_name => 'create_parameters_configuration',
				       );
    }
}
 
  

sub version {
    my ($self) = @_;
    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
        method => "QIIME.version",
        params => [],
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(
                error => $result->error_message,
                code => $result->content->{code},
                method_name => 'create_parameters_configuration',
            );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(
            error => "Error invoking method create_parameters_configuration",
            status_line => $self->{client}->status_line,
            method_name => 'create_parameters_configuration',
        );
    }
}

sub _validate_version {
    my ($self) = @_;
    my $svr_version = $self->version();
    my $client_version = $VERSION;
    my ($cMajor, $cMinor) = split(/\./, $client_version);
    my ($sMajor, $sMinor) = split(/\./, $svr_version);
    if ($sMajor != $cMajor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Major version numbers differ.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor < $cMinor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Client minor version greater than Server minor version.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor > $cMinor) {
        warn "New client version available for QIIME::QIIMEClient\n";
    }
    if ($sMajor == 0) {
        warn "QIIME::QIIMEClient version is $svr_version. API subject to change.\n";
    }
}

=head1 TYPES



=head2 handle_id

=over 4



=item Description

@id handle


=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 FastaHandle

=over 4



=item Description

@optional remote_md5
@optional remote_sha1


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
hid has a value which is a QIIME.handle_id
file_name has a value which is a string
id has a value which is a string
url has a value which is a string
remote_md5 has a value which is a string
remote_sha1 has a value which is a string
size has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
hid has a value which is a QIIME.handle_id
file_name has a value which is a string
id has a value which is a string
url has a value which is a string
remote_md5 has a value which is a string
remote_sha1 has a value which is a string
size has a value which is an int


=end text

=back



=head2 PostSplitLibrary

=over 4



=item Description

Handle to a FASTA file in the QIIME post-split library file format.
see http://qiime.org/documentation/file_formats.html#post-split-libraries-fasta-file-overview

@metadata ws fasta.file_name as Filename
@metadata ws fasta.size as File Size
@metadata ws fasta.remote_md5 as File MD5
@metadata ws fasta.remote_sha1 as File SHA1


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
fasta has a value which is a QIIME.FastaHandle

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
fasta has a value which is a QIIME.FastaHandle


=end text

=back



=head2 BIOMHandle

=over 4



=item Description

@optional remote_md5
@optional remote_sha1


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
hid has a value which is a QIIME.handle_id
file_name has a value which is a string
id has a value which is a string
url has a value which is a string
remote_md5 has a value which is a string
remote_sha1 has a value which is a string
size has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
hid has a value which is a QIIME.handle_id
file_name has a value which is a string
id has a value which is a string
url has a value which is a string
remote_md5 has a value which is a string
remote_sha1 has a value which is a string
size has a value which is an int


=end text

=back



=head2 QIIMEParameters

=over 4



=item Description

@metadata ws length(lines) as N Lines


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
lines has a value which is a reference to a list where each element is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
lines has a value which is a reference to a list where each element is a string


=end text

=back



=head2 OTUTable

=over 4



=item Description

OTU Table, generally a wrapper of a BIOM file 

        TODO: add:
            int n_samples;
            int n_observations;
            int count;
            float density;

            mapping<string,float> sample_detail;
        @metadata ws summary as Summary


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
biom has a value which is a QIIME.BIOMHandle
summary has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
biom has a value which is a QIIME.BIOMHandle
summary has a value which is a string


=end text

=back



=head2 PickClosedRefOTUsParams

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
workspace has a value which is a string
post_split_lib has a value which is a string
otu_table_name has a value which is a string
parameters_config has a value which is a string
rev_strand_match has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
workspace has a value which is a string
post_split_lib has a value which is a string
otu_table_name has a value which is a string
parameters_config has a value which is a string
rev_strand_match has a value which is an int


=end text

=back



=head2 PickClosedRefOTUsResults

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
otu_table_ref has a value which is a string
report_name has a value which is a string
report_ref has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
otu_table_ref has a value which is a string
report_name has a value which is a string
report_ref has a value which is a string


=end text

=back



=head2 CreateParametersConfigurationParams

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
workspace has a value which is a string
name has a value which is a string
content has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
workspace has a value which is a string
name has a value which is a string
content has a value which is a string


=end text

=back



=head2 CreateParametersConfigurationResults

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
report_name has a value which is a string
report_ref has a value which is a string
parameters_configuration_ref has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
report_name has a value which is a string
report_ref has a value which is a string
parameters_configuration_ref has a value which is a string


=end text

=back



=cut

package QIIME::QIIMEClient::RpcClient;
use base 'JSON::RPC::Client';
use POSIX;
use strict;

#
# Override JSON::RPC::Client::call because it doesn't handle error returns properly.
#

sub call {
    my ($self, $uri, $headers, $obj) = @_;
    my $result;


    {
	if ($uri =~ /\?/) {
	    $result = $self->_get($uri);
	}
	else {
	    Carp::croak "not hashref." unless (ref $obj eq 'HASH');
	    $result = $self->_post($uri, $headers, $obj);
	}

    }

    my $service = $obj->{method} =~ /^system\./ if ( $obj );

    $self->status_line($result->status_line);

    if ($result->is_success) {

        return unless($result->content); # notification?

        if ($service) {
            return JSON::RPC::ServiceObject->new($result, $self->json);
        }

        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    elsif ($result->content_type eq 'application/json')
    {
        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    else {
        return;
    }
}


sub _post {
    my ($self, $uri, $headers, $obj) = @_;
    my $json = $self->json;

    $obj->{version} ||= $self->{version} || '1.1';

    if ($obj->{version} eq '1.0') {
        delete $obj->{version};
        if (exists $obj->{id}) {
            $self->id($obj->{id}) if ($obj->{id}); # if undef, it is notification.
        }
        else {
            $obj->{id} = $self->id || ($self->id('JSON::RPC::Client'));
        }
    }
    else {
        # $obj->{id} = $self->id if (defined $self->id);
	# Assign a random number to the id if one hasn't been set
	$obj->{id} = (defined $self->id) ? $self->id : substr(rand(),2);
    }

    my $content = $json->encode($obj);

    $self->ua->post(
        $uri,
        Content_Type   => $self->{content_type},
        Content        => $content,
        Accept         => 'application/json',
	@$headers,
	($self->{token} ? (Authorization => $self->{token}) : ()),
    );
}



1;
