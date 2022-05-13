import React, { useContext, useEffect, useState } from "react";
import { GaodeMap, Mapbox } from '@antv/l7-maps';
import data from "./mock-data";
import { Scene, PointLayer } from '@antv/l7';
import Stack from "@mui/material/Stack";
import ArrowLeftIcon from '@mui/icons-material/ArrowLeft';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';
import Box from "@mui/system/Box";
import IconButton from "@mui/material/IconButton";
import { fetchHousePriceData } from "../../services/services";
import { DataDisplayContext } from "../../App";

const HousePriceAnalysisPanel = () => {
  const [arleadyLoadMap, setAlreadyLoadMap] = useState(false)
  const [selectedTime, setSelectedTime] = useState(0)
  const [allTimeSlots, setAllTimeSlots] = useState<string[]>([])
  const [housePriceData, setHousePriceData] = useState<any>({})
  const {displayOptions: {houseType, priceType}} = useContext(DataDisplayContext)
  const [displayData, setDisplayData] = useState<any>({})

  useEffect(() => {
    fetchHousePriceData()
    .then(JSONData => {
      const JSONHousePriceData = JSONData.filter((jd: { name: string; }) => jd.name === "aurin_house_price")[0].details 
      setAllTimeSlots(Object.keys(JSONHousePriceData))
      // setAllTimeSlots(Object.values(JSONData))
      setHousePriceData(JSONHousePriceData)
    }
    )
  }, [])

  useEffect(() => {
    const scene = new Scene({
      id: 'housePrice-analysis-heatMap',
      map: new Mapbox({
        pitch: 0,
        style: 'light',
        center: [ 144.92874662745265, -37.81343237141352 ],
        zoom: 9.9,
        maxZoom: 10
      })
    });
    scene.on('loaded', () => {
      const pointLayer = new PointLayer({})
        .source(displayData)
        .shape('circle')
        .size('price', [ 30, 56 ])
        .color('price', [
          '#F39E9E',
          '#F49393',
          '#F38E8E',
          '#F16363',
          '#ED4343',
          '#70505'
        ])
        .active(true)
        .style({
          opacity: 0.5,
          strokeWidth: 0
        });
      scene.addLayer(pointLayer);
    });
    return () => {scene.destroy()}
  }, [displayData])

  useEffect(() => {
    if(housePriceData[allTimeSlots[selectedTime]]? housePriceData[allTimeSlots[selectedTime]][houseType]: undefined) {
      const d = housePriceData[allTimeSlots[selectedTime]][houseType]
      data.features = data.features.map(feature => {
        // console.log(d[feature.name])
        // console.log(d[feature.name][priceType])
        if(d[feature.name]? d[feature.name][priceType]: undefined) {
          feature.properties.price = d[feature.name][priceType]
        }
        return feature})
      console.log('update data')
      setDisplayData(data)
    }
  }, [selectedTime, houseType])

  const setNextYear = () => {
    if(selectedTime < allTimeSlots.length - 1) {
      setSelectedTime(selectedTime + 1)
    }
  }

  const setPreviousYear = () => {
    if(selectedTime > 0) {
      setSelectedTime(selectedTime - 1)
    }
  }

  return (
    <Stack direction='column' spacing={2} alignItems='center' justifyContent='center'>
      <Stack direction='row' spacing={2}>
        <IconButton onClick={() => {setPreviousYear()}}>
          <ArrowLeftIcon/>
        </IconButton>
        <Box style={{display: 'flex', alignItems: 'center'}}>
          {allTimeSlots[selectedTime]}
        </Box>
        <IconButton onClick={() => {setNextYear()}}>
          <ArrowRightIcon/>
        </IconButton>
      </Stack>
      <div id='housePrice-analysis-heatMap' style={{height: '80vh', width: '80vw',justifyContent: 'center', position: 'relative' }}/>
    </Stack>
  )
}

export default HousePriceAnalysisPanel