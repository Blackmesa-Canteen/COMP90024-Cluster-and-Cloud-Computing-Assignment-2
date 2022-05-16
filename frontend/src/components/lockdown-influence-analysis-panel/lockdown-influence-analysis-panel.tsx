import { Console } from "console";
import React, { useContext, useEffect, useState } from "react";
import { fetchCovidData } from "../../services/services";
import { Chart } from '@antv/g2';
import Stack from "@mui/material/Stack";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from '@mui/material/Typography';
import { DataDisplayContext } from "../../App";



const LockdownInfluenceAnalysisPanel = () => {
  const { selectedScenario } = useContext(DataDisplayContext)
  const [unEmploymentCount, setUnEmploymentCount] = useState<any[]>([])
  const [unEmploymentRate, setUnEmploymentRate] = useState<any[]>([])
  const [employmentCount, setEmploymentCount] = useState<any[]>([])
  const [totalPolarity, setTotalPolarity] = useState<any[]>([])
  const [lockDownPolarity, setLockDownPolarity] = useState<any[]>([])

  useEffect(() => {
    fetchCovidData()
    .then(JSONData => {
      console.log('lock down')
      setUnEmploymentCount(
        Object.entries(JSONData.filter((jd: {name: string}) => jd.name === "unemployment")[0].details)
        .map(keyValue => ({
          xValue: keyValue[0],
          yValue: keyValue[1],
        }))
      )
      setUnEmploymentRate(
        Object.entries(JSONData.filter((jd: {name: string}) => jd.name === "unemployment_rate")[0].details)
        .map(keyValue => ({
          xValue: keyValue[0],
          yValue: keyValue[1],
        }))
      )
      setEmploymentCount(
        Object.entries(JSONData.filter((jd: {name: string}) => jd.name === "employment")[0].details)
        .map(keyValue => ({
          xValue: keyValue[0],
          yValue: keyValue[1],
        }))
      )
      setTotalPolarity(
        Object.entries(JSONData.filter((jd: {name: string}) => jd.name === "total_polarity")[0].details)
        .map(keyValue => ({
          xValue: keyValue[0],
          yValue: keyValue[1],
        }))
      )
      setLockDownPolarity(
        Object.entries(JSONData.filter((jd: {name: string}) => jd.name === "lockdowm_polarity")[0].details)
        .map(keyValue => ({
          xValue: keyValue[0],
          yValue: keyValue[1],
        }))
      )
    })
  }, [])

  useEffect(() => {
    const chart_unemployment = new Chart({
      container: 'container_unemployment',
      autoFit: true,
      height: 500,
    });
    chart_unemployment.data(unEmploymentRate);
    chart_unemployment.scale({
      xValue: {
        tickCount: 10
      },
      yValue: {
        nice: true,
      }
    });
    chart_unemployment.axis('xValue', {
      label: {
        formatter: text => text
      }
    });

    chart_unemployment.line().position('xValue*yValue');
    chart_unemployment.render();
    return () => {chart_unemployment.destroy()}
  }, [unEmploymentCount])

  useEffect(() => {
    const chart_unemployment_rate = new Chart({
      container: 'container_unemployment_rate',
      autoFit: true,
      height: 500,
    });
    chart_unemployment_rate.data(unEmploymentCount);
    chart_unemployment_rate.scale({
      xValue: {
        tickCount: 10
      },
      yValue: {
        nice: true,
      }
    });
    chart_unemployment_rate.axis('xValue', {
      label: {
        formatter: text => text
      }
    });

    chart_unemployment_rate.line().position('xValue*yValue');
    chart_unemployment_rate.render();
    return () => {chart_unemployment_rate.destroy()}
  }, [unEmploymentRate])
  
  useEffect(() => {
    const chart_unemployment_rate = new Chart({
      container: 'container_employment_count',
      autoFit: true,
      height: 500,
    });
    chart_unemployment_rate.data(employmentCount);
    chart_unemployment_rate.scale({
      xValue: {
        tickCount: 10
      },
      yValue: {
        nice: true,
      }
    });
    chart_unemployment_rate.axis('xValue', {
      label: {
        formatter: text => text
      }
    });

    chart_unemployment_rate.line().position('xValue*yValue');
    chart_unemployment_rate.render();
    return () => {chart_unemployment_rate.destroy()}
  }, [employmentCount])

  useEffect(() => {
    const chart_unemployment_rate = new Chart({
      container: 'container_sentimental_rate',
      autoFit: true,
      height: 500,
    });
    chart_unemployment_rate.data(totalPolarity);
    chart_unemployment_rate.scale({
      xValue: {
        tickCount: 10
      },
      yValue: {
        nice: true,
      }
    });
    chart_unemployment_rate.axis('xValue', {
      label: {
        formatter: text => text
      }
    });

    chart_unemployment_rate.line().position('xValue*yValue');
    chart_unemployment_rate.render();
    return () => {chart_unemployment_rate.destroy()}
  }, [totalPolarity])

  useEffect(() => {
    const chart_unemployment_rate = new Chart({
      container: 'lockdown_date_sentimental_rate',
      autoFit: true,
      height: 500,
    });
    chart_unemployment_rate.data(lockDownPolarity);
    chart_unemployment_rate.scale({
      xValue: {
        tickCount: 10
      },
      yValue: {
        nice: true,
      }
    });
    chart_unemployment_rate.axis('xValue', {
      label: {
        formatter: text => text
      }
    });

    chart_unemployment_rate.line().position('xValue*yValue');
    chart_unemployment_rate.render();
    return () => {chart_unemployment_rate.destroy()}
  }, [lockDownPolarity])

  return (
    <Stack direction='column' spacing={4}>
      <Stack direction='row' spacing={2}>
        <Card key='container_unemployment_card'>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div" sx={{marginBottom: '15px'}}>
              Unemployment Rate
            </Typography>
            <div id="container_unemployment"  style={{ width: '35vw', height: '30vh'}}></div>
          </CardContent>
        </Card>
        <Card key='container_unemployment_rate_card'>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div" sx={{marginBottom: '15px'}}>
              Unemployment Count
            </Typography>
            <div id="container_unemployment_rate" style={{ width: '35vw', height: '30vh'}}></div>
          </CardContent>
        </Card>
      </Stack>
      <Stack direction='row' spacing={2}>
        <Card key='container_employment_count_card'>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div" sx={{marginBottom: '15px'}}>
              Employment Count
            </Typography>
            <div id="container_employment_count" style={{ width: '35vw', height: '30vh'}}></div>
          </CardContent>
        </Card>
        <Card key='container_sentimental_rate_card'>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div" sx={{marginBottom: '15px'}}>
              Sentimental Rate
            </Typography>
            <div id="container_sentimental_rate" style={{ width: '35vw', height: '30vh'}}></div>
          </CardContent>
        </Card>
      </Stack>
      
      <Card key='lockdown_date_sentimental_rate_card'>
        <CardContent>
          <Typography gutterBottom variant="h5" component="div" sx={{marginBottom: '15px'}}>
            Lockdown Date Sentimental Rate
          </Typography>
          <div id="lockdown_date_sentimental_rate" style={{ width: '100%', height: '30vh'}}></div>
        </CardContent>
      </Card>
    </Stack>
  )
}

export default LockdownInfluenceAnalysisPanel;