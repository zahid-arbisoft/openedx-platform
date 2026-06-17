# Studio SSO Client-ID Alignment

The example client ID in the CMS SSO setup section should use 'studio-sso-key' as the example client ID.

## Example Configuration

```yaml
SOCIAL_AUTH_EDX_OAUTH2_KEY = 'studio-sso-key'
```

## Testing

To verify that the updated README matches the default value of 'SOCIAL_AUTH_EDX_OAUTH2_KEY' in 'cms/envs/devstack.py:277', run the following command:

```sh
pytest
```