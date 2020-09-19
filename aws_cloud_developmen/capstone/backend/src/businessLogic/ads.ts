import * as uuid from 'uuid'
import { AdItem } from '../models/AdItem'
import { AdAccess } from '../dataLayer/adAccess'
import { CreateAdRequest } from '../requests/CreateAdRequest'
import { UpdateAdRequest } from '../requests/UpdateAdRequest'
import { parseUserId } from '../auth/utils'
import { AdUpdate } from '../models/AdUpdate'
import { AdS3 } from '../dataLayer/adS3'


const adAccess = new AdAccess()
const s3Access = new AdS3()

export async function getUserAdItems(jwtToken: string): Promise<AdItem[]> {
  const userId = parseUserId(jwtToken)
  return adAccess.getUserAdItems(userId)
}

export async function getAllAdItems(): Promise<AdItem[]> {
  return await adAccess.getAllAdItems()
}

export async function deleteAdItem(jwtToken:string,adId: string): Promise<AdItem[]> {
  const userId = parseUserId(jwtToken)
  return await adAccess.deleteAdItem(userId,adId)
}
export async function updateAdItem(jwtToken:string,adId: string, updateAdItem: UpdateAdRequest): Promise<any> {
  const userId = parseUserId(jwtToken)
  updateAdItem as AdUpdate
  return await adAccess.updateAdItem(userId,adId,updateAdItem)
}
export async function createAdItem(
  createAdRequest: CreateAdRequest,
  jwtToken: string
): Promise<AdItem> {

  const itemId = uuid.v4()
  const userId = parseUserId(jwtToken)

  return await adAccess.createAdItem({
    adId: itemId,
    userId: userId,
    name: createAdRequest.name,
    createdAt: new Date().toISOString(),
    location: createAdRequest.location,
    email: createAdRequest.email,
    price: createAdRequest.price
  })
}

export async  function generateImageURL(
  adId: string,
  jwtToken: string
): Promise<string> {
  const {url, bucketName} = JSON.parse(s3Access.generateImageURL(adId))
  const userId = parseUserId(jwtToken)
  await adAccess.updateImageURL(userId, adId, bucketName)
  return url
}

