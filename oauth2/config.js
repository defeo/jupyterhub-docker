module.exports = {
    // The URL where the OAuth2 server will respond
    appURL: "https://jupyter.ens.uvsq.fr/c2o2b",
    // The port to bind to
    port: process.env.PORT,

    // The endpoints of the CAS server (v1.0) to authenticate to
    cas: {
	entryPoint: "https://cas.uvsq.fr/login",
	validate: "https://cas.uvsq.fr/serviceValidate",
    },
    // The endpoint of the SAML server (v2.0) to authenticate to
    saml: {
	entryPoint: "https://cas.uvsq.fr/login",
	issuer: "cas2oauth2bridge",
    },
    
    // The cipher used to encrypt cookies
    crypto: {
	// Authenticated encryption mode
	algorithm: "aes-256-gcm",
	// If initialized to zero, like here, a random key will be
	// generated at startup (hence, cookies will not survive
	// reboot).
	key: Buffer.alloc(32),
	ivlen: 16,
    },
    
    // Definition of the services
    oauth: {
	// Expiration time of authentication cookies
	tokenLifetime: 24*60*60,
	// The services allowed to authenticate to this server
	clients: {
	    "0": {
		secret: null,
		redirectUri: new RegExp('^https://jupyter\\.ens\\.uvsq\\.fr/'),
	    },
	},
    },
}
