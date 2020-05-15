import axios from 'axios'

export default class BackendService {
  baseDomain = "https://aigames-fearless-gerenuk-kq.cfapps.io"
  baseURL = `${this.baseDomain}`

  constructor() {}

  startGame() {
    return axios
      .post(`${(this.baseURL)}/nim`)
  }

  submitAction(id, pileSelected, numberOfDots) {
    let requestConfig = {
        headers: { 'Content-Type': 'application/json' }
      }
    let body = {'pile': pileSelected, 'number': numberOfDots}
    return axios
        .put(`${this.baseURL}/nim/${id}`, body, requestConfig)
  }

}