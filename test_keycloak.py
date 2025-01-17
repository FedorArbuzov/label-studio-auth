from keycloak import KeycloakOpenID

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8081/auth/",
                                 client_id="fedor2",
                                 realm_name="test",
                                 client_secret_key="ngFPQIpzE54Eb1C2SRH0ssrjgjUTLKqj")


print(keycloak_openid)

# Get WellKnown
# config_well_known = keycloak_openid.well_known()

# # Get Code With Oauth Authorization Request
# auth_url = keycloak_openid.auth_url(
#     redirect_uri="your_call_back_url",
#     scope="email",
#     state="your_state_info")

# # Get Access Token With Code
# access_token = keycloak_openid.token(
#     grant_type='authorization_code', 
#     code='the_code_you_get_from_auth_url_callback',
#     redirect_uri="your_call_back_url")


# Get Token
token = keycloak_openid.token(username="test_admin", password="TESTpSSWrd")
print(token)
#token = keycloak_openid.token("user", "password", totp="012345")

# Get token using Token Exchange
token = keycloak_openid.exchange_token(token['access_token'], "my_client", "other_client", "some_user")

# Get Userinfo
userinfo = keycloak_openid.userinfo(token['access_token'])

# Refresh token
token = keycloak_openid.refresh_token(token['refresh_token'])

# Logout
keycloak_openid.logout(token['refresh_token'])