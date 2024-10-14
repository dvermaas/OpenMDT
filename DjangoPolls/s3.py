from storages.backends.s3boto3 import S3Boto3Storage


class CustomDomainFixedUpS3Boto3Storage(S3Boto3Storage):
    # work around for url + custom domains not working for pre-signed urls.
    # see: https://github.com/jschneier/django-storages/issues/165#issuecomment-810166563
    # adapted to preserve the inputs we would expect to use if this were fixed upstream.
    x_custom_domain = None
    x_url_protocol = "https:"

    def url(self, name, parameters=None, expire=None, http_method=None):
        """Replace internal domain with custom domain for signed URLs."""
        url = super().url(name, parameters, expire, http_method)
        if self.x_custom_domain:
            return url.replace(
                self.endpoint_url,
                f"{self.x_url_protocol}//{self.x_custom_domain}",
            )
        return url
