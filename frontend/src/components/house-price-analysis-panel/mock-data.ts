// const data = {
//   "type": "FeatureCollection",
//   "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
//   "features": [  
//     {"type": "Feature", 
//       "properties": { 
//         "id": "pr2017261001", 
//         "name": "Melbourne - Inner",
//         "price": 55551,}, 
//         "geometry": { 
//           "type": "Point", 
//           "coordinates": [ -64.7745, 18.8611, ] }},
//   ]
//   }
  
  // const data = {
  //   "type": "FeatureCollection",
  //   "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
  //   "features": [  
  //     {"type": "Feature", 
  //       "properties": { 
  //         "id": "pr2017261001", 
  //         "name": "Melbourne - Inner",
  //         "price": 55551,}, 
  //         "geometry": { 
  //           "type": "Point", 
  //           "coordinates": [ -64.7745, 18.8611, 60.0 ] }},
  //   ]
  //   }
const data = {
  "type": "FeatureCollection",
  "features": [
    {
      name: 'Melbourne - Inner',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 144.92874662745265, -37.81343237141352 ]
      },
      "properties": {
      "price":521684.3,
      }
    },
    {
      name: 'Melbourne - Inner East',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 145.01465383001445, -37.81601449715302 ]
      },
      "properties": {
      "price":441439.2,
      }
    },
    {
      name: 'Melbourne - Inner South',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 145.0013736823581, -37.88713722205395 ]
      },
      "properties": {
      "price":6720,
      }
    },
    {
      name: 'Melbourne - North East',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 145.10876965905746, -37.7320380000303 ]
      },
      "properties": {
      "price":6720,
      }
    },
    {
      name: 'Melbourne - North West',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 144.922270194144, -37.713312853354175 ]
      },
      "properties": {
      "price":6720,
      }
    },
    {
      name: 'Melbourne - Outer East',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 145.219630022102, -37.826504851657 ]
      },
      "properties": {
      "price":6720,
      }
    },
    {
      name: 'Melbourne - South East',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 145.11626466491896, -37.944728858607014 ]
      },
      "properties": {
      "price":6720,
      }
    },
    {
      name: 'Melbourne - West',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 144.81821891718084, -37.818407158660825 ]
      },
      "properties": {
      "price":6720,
      }
    },
    {
      name: 'Mornington Peninsula',
      "type": "Feature",
      "geometry": {
         "type": "Point",
         "coordinates":  [ 144.75289382178616, -37.875149824765614 ]
      },
      "properties": {
      "price":6720,
      }
    },
  ]
}

export default data