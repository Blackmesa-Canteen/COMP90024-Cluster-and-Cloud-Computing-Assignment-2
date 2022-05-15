export const fetchPopulationData = () => {
  return fetch('http://172.26.135.17:80/api/scenario/languages', {mode: 'cors'})
  .then(async (data) => {
    const JSONData = await data.json()
    return JSONData
  })
}

export const fetchLanguagesCountData = () => {
  return fetch('http://172.26.135.17:80/api/scenario/languages-month', {mode: 'cors'})
    .then(async (data) => {
      const JSONData = await data.json()
      return JSONData
    })
}

export const fetchCovidData = () => {
  return fetch('http://172.26.135.17:80/api/scenario/covid', {mode: 'cors'})
    .then(async (data) => {
      const JSONData = await data.json()
      return JSONData
    })
}

export const fetchHousePriceData = () => {
  return fetch('http://172.26.135.17:80/api/scenario/house-price', {mode: 'cors'})
    .then(async (data) => {
      const JSONData = await data.json()
      return JSONData
    })
}

export const fetchTwitter = () => {
  return fetch('http://172.26.135.17:80/api/scenario/stream', {mode: 'cors'})
    .then(async (data) => {
      const JSONData = await data.json()
      return JSONData
    })
}