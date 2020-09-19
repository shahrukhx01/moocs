# Serverless UDALIST - An AD Posting Platform

I implemented a simple AD application using AWS Lambda and Serverless framework.

# Functionality of the application

This application will allow creating/removing/updating/fetching AD items. Each AD item can optionally have an attachment image. Each user only has access to AD items that he/she has created and created by others but the user can only edit/delete his/her own ads only.

# AD items

The application stores AD items, and each AD item contains the following fields:

* `adId` (string) - a unique id for an item
* `location` (string) - location of the item
* `email` (string) - email of the ad poster
* `createdAt` (string) - date and time when an item was created
* `name` (string) - name of a AD item (e.g. "Bicycle for sale")
* `price` (string) - price of the item (i.e $100)
* `attachmentUrl` (string) (optional) - a URL pointing to an image attached to a AD item

I also stored an id of a user who created a AD item.


# Functions implemented

I implemented the following functions and configured them in the `serverless.yml` file:

* `Auth` - this function should implement a custom authorizer for API Gateway that should be added to all other functions.

* `GetUserAds` - should return all ADs for a current user. A user id can be extracted from a JWT token that is sent by the frontend

It should return data that looks like this:

```json
{
    "items": [
        {
            "location": "Berlin",
            "adId": "dccf1b89-2995-45d2-8d7b-798113402a42",
            "userId": "google-oauth2|116144351300130652456",
            "attachmentUrl": "https://sls-ad-images-dev.s3.amazonaws.com/dccf1b89-2995-45d2-8d7b-798113402a42",
            "createdAt": "2020-05-13T00:15:35.572Z",
            "price": 100,
            "email": "ad_owner22@gmail.com",
            "name": "Haze flowers"
        }
    ]
}
```

* `GetAllAds` - should return all ADs for all users.

It should return data that looks like this:

```json
{
    "items": [
        {
            "location": "Berlin",
            "adId": "75bb0cdc-d3ab-4864-8efc-ff317850f45a",
            "userId": "google-oauth2|113835315038848972126",
            "createdAt": "2020-05-13T00:11:00.942Z",
            "price": 100,
            "email": "ad_owner3@gmail.com",
            "name": "rose flowers"
        },
        {
            "location": "Oslo",
            "adId": "86f44afb-bc58-4b70-93ff-c53921fff668",
            "userId": "google-oauth2|113835315038848972126",
            "createdAt": "2020-05-13T00:04:35.639Z",
            "price": 1100,
            "email": "ad_owner@gmail.com",
            "name": "Water flowers"
        },
        {
            "location": "Berlin",
            "adId": "cc2b0786-b302-4d7b-aa30-2c1a0002b14b",
            "userId": "google-oauth2|113835315038848972126",
            "createdAt": "2020-05-13T00:05:08.143Z",
            "price": 100,
            "email": "ad_owner2@gmail.com",
            "name": "Sun flowers"
        },
        {
            "location": "Berlin",
            "adId": "dccf1b89-2995-45d2-8d7b-798113402a42",
            "attachmentUrl": "https://sls-ad-images-dev.s3.amazonaws.com/dccf1b89-2995-45d2-8d7b-798113402a42",
            "userId": "google-oauth2|116144351300130652456",
            "createdAt": "2020-05-13T00:15:35.572Z",
            "email": "ad_owner22@gmail.com",
            "price": 100,
            "name": "Haze flowers"
        }
    ]
}
```

* `CreateAd` - should create a new AD for a current user. A shape of data send by a client application to this function can be found in the `CreateAdRequest.ts` file

It receives a new AD item to be created in JSON format that looks like this:

```json
{
	"name": "Camera",
	"price": 1000,
	"location": "Berlin",
	"email": "ad_owner99@gmail.com"
}
```

It should return a new AD item that looks like this:

```json
{
    "item": {
        "adId": "02fa0da5-b83a-4465-8b7e-56daa00f54e6",
        "userId": "google-oauth2|116144351300130652456",
        "name": "Camera",
        "createdAt": "2020-05-13T00:52:54.992Z",
        "location": "Berlin",
        "email": "ad_owner99@gmail.com",
        "price": 1000
    }
}
```

* `UpdateAd` - should update a AD item created by a current user. A shape of data send by a client application to this function can be found in the `UpdateAdRequest.ts` file

It receives an object that contains three fields that can be updated in a AD item:

```json
{
	"name": "DSLR",
	"price": 800,
	"location": "Stockholm",
	"email": "new_ad_owner21@gmail.com"
}
```

The id of an item that should be updated is passed as a URL parameter.

It should return an empty body.

* `DeleteAD` - should delete a AD item created by a current user. Expects an id of a AD item to remove.

It should return an empty body.

* `GenerateUploadUrl` - returns a pre-signed URL that can be used to upload an attachment file for a AD item.

It should return a JSON object that looks like this:

```json
{
  "uploadUrl": "https://s3-bucket-name.s3.eu-west-2.amazonaws.com/image.png"
}
```

All functions are already connected to appropriate events from API Gateway.

An id of a user can be extracted from a JWT token passed by a client.

You also need to add any necessary resources to the `resources` section of the `serverless.yml` file such as DynamoDB table and S3 bucket.


# Frontend

The `client` folder contains a web application that can use the API that should be developed in the project.

This frontend should work with your serverless application once it is developed, you don't need to make any changes to the code. The only file that you need to edit is the `config.ts` file in the `client` folder. This file configures your client application just as it was done in the course and contains an API endpoint and Auth0 configuration:

```ts
const apiId = '...' API Gateway id
export const apiEndpoint = `https://${apiId}.execute-api.us-east-1.amazonaws.com/dev`

export const authConfig = {
  domain: '...',    // Domain from Auth0
  clientId: '...',  // Client id from an Auth0 application
  callbackUrl: 'http://localhost:3000/callback'
}
```

## Authentication

To implement authentication in your application, you would have to create an Auth0 application and copy "domain" and "client id" to the `config.ts` file in the `client` folder. We recommend using asymmetrically encrypted JWT tokens.


# How to run the application

## Backend

To deploy an application run the following commands:

```
cd backend
npm install
sls deploy -v
```

## Frontend

To run a client application first edit the `client/src/config.ts` file to set correct parameters. And then run the following commands:

```
cd client
npm install
npm run start
```

This should start a development server with the React application that will interact with the serverless AD application.

# Postman collection

I have created a Postman collection to test endpoints separately the name of collection file is `Capstone.postman_collection.json`
