import { CustomAuthorizerEvent, CustomAuthorizerResult } from 'aws-lambda'
import 'source-map-support/register'

import { verify } from 'jsonwebtoken'
import { createLogger } from '../../utils/logger'
//import Axios from 'axios'
//import { Jwt } from '../../auth/Jwt'
import { JwtPayload } from '../../auth/JwtPayload'

const logger = createLogger('auth')

const cert = `-----BEGIN CERTIFICATE-----
MIIDBzCCAe+gAwIBAgIJaH0mlm74vwFRMA0GCSqGSIb3DQEBCwUAMCExHzAdBgNV
BAMTFmRldi00c2RiY3k4My5hdXRoMC5jb20wHhcNMjAwNTEwMjAzMjQyWhcNMzQw
MTE3MjAzMjQyWjAhMR8wHQYDVQQDExZkZXYtNHNkYmN5ODMuYXV0aDAuY29tMIIB
IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4p9qK5C6aURPgLiD+pZn+3fX
IsM9Cfpwgoj9AnDD5Ef+riMAn6vsm7viOewyqGzqzrq5Xn3X8vwLXEkmdflAPCus
XPXRrGqQvZxly/ZZYwoSo+dKuMHf+HShtktTUNeTGmPtCsB28wpXyK4fDFUdVNSF
+tMKGXvwvxTUXcaIIyv01I8or/L0Xxevls9PEGW+mPPbiYZTzZLVknu/3LDUNuWR
NnNlWRTkJ4UwExLd61Kg1LuutvLDU8kK/esmViLOb/e3wqVTjr9bQal5dsG7Bjse
m4ZX55Kn9Ftzk2RxjDRW3D2lwsBu9jdrzKYph25vw0N50QKTvwke7HRkiGWDqQID
AQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBT4+986OBeeaMGE6CM1
6ULqR/yH8TAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBAGIjfG7I
tQSiDqWm745X72xHqhkR8AqK1LC/WZCPfRgl7uYTDuXvCg8c9qlcbBOEAj6TIi+J
8FHWUgC0mKRz+yOk7HQTxW9tOmkQ4PtBF48zgYUDxB0spfmsMi7LJ1rLkgRItJMN
OvuljpL+Z0bIyxRaVb/05SzSkAndhsGyv+glnBYJcJjgjSnXKB9Fl/V+jZ5BM0+f
ZGlyt4XBKUh3gpwJZt4jUwYQfhB8zCTJz0XZCdoU/pBTdQSTuFE2ZtbYHORNMtrJ
A7ZPj2BL879zu4zQcrdxA759o0XlbNwRS0gBwBRC4PLMpv9DUFkVwcYqO9M1Q/CZ
s8U7GSa6andk8zs=
-----END CERTIFICATE-----`

// TODO: Provide a URL that can be used to download a certificate that can be used
// to verify JWT token signature.
// To get this URL you need to go to an Auth0 page -> Show Advanced Settings -> Endpoints -> JSON Web Key Set
//const jwksUrl = 'https://dev-4sdbcy83.auth0.com/.well-known/jwks.json'

export const handler = async (
  event: CustomAuthorizerEvent
): Promise<CustomAuthorizerResult> => {
  logger.info('Authorizing a user', event.authorizationToken)
  try {
    const jwtToken = await verifyToken(event.authorizationToken)
    logger.info('User was authorized', jwtToken)

    return {
      principalId: jwtToken.sub,
      policyDocument: {
        Version: '2012-10-17',
        Statement: [
          {
            Action: 'execute-api:Invoke',
            Effect: 'Allow',
            Resource: '*'
          }
        ]
      }
    }
  } catch (e) {
    logger.error('User not authorized', { error: e.message })

    return {
      principalId: 'user',
      policyDocument: {
        Version: '2012-10-17',
        Statement: [
          {
            Action: 'execute-api:Invoke',
            Effect: 'Deny',
            Resource: '*'
          }
        ]
      }
    }
  }
}

async function verifyToken(authHeader: string): Promise<JwtPayload> {
  const token = getToken(authHeader)
  //const jwt: Jwt = decode(token, { complete: true }) as Jwt
  //const jwksPayload =  Axios.get(jwksUrl)
  //const certurl =  jwksPayload['keys'][0]['x5c'][0]
  //console.log(`cert ${certurl}`)

  // TODO: Implement token verification
  // You should implement it similarly to how it was implemented for the exercise for the lesson 5
  // You can read more about how to do this here: https://auth0.com/blog/navigating-rs256-and-jwks/
  return verify(token, cert, { algorithms: ['RS256'] }) as JwtPayload
}

function getToken(authHeader: string): string {
  if (!authHeader) throw new Error('No authentication header')

  if (!authHeader.toLowerCase().startsWith('bearer '))
    throw new Error('Invalid authentication header')

  const split = authHeader.split(' ')
  const token = split[1]

  return token
}
