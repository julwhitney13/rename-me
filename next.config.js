/** @type {import('next').NextConfig} */
const nextConfig = {
// async rewrites() {
//     return [
//         {
//             source: '/api/:path*',
//             destination: 'http://localhost:5000/:path*' // Proxy to Backend
//         }
//     ]
//     }
    publicRuntimeConfig: {
    // Will be available on both server and client
        API_URL: process.env.API_URL,
    }
}

module.exports = nextConfig
