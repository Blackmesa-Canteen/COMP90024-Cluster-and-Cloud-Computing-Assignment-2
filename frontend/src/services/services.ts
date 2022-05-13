export const fetchPopulationData = () => {
  return fetch('http://localhost:5000/api/scenario/languages', {mode: 'cors'})
  .then(async (data) => {
    const JSONData = await data.json()
    return JSONData
  })
}

export const fetchLanguagesCountData = () => {
  return fetch('http://localhost:5000/api/scenario/languages-month', {mode: 'cors'})
    .then(async (data) => {
      const JSONData = await data.json()
      return JSONData
    })
}

export const fetchCovidData = () => {
  return fetch('http://localhost:5000/api/scenario/covid', {mode: 'cors'})
    .then(async (data) => {
      const JSONData = await data.json()
      return JSONData
    })
}

export const fetchHousePriceData = () => {
  return fetch('http://localhost:5000/api/scenario/house-price', {mode: 'cors'})
    .then(async (data) => {
      const JSONData = await data.json()
      return JSONData
    })
}