import React, { useEffect, useState } from "react";
import { Pie } from '@antv/g2plot';
import Stack from "@mui/material/Stack";
import { fetchTwitter } from "../../services/services";
import Card from "@mui/material/Card";
import Typography from "@mui/material/Typography";
import CardContent from "@mui/material/CardContent";
import { CardActions } from "@mui/material";

const TwitterAnalysisOptionPanel = () => {
  const [polarityData, setPolarityData] = useState<{
    type: string;
    value: number;
}[]>([{ type: '分类一', value: 27 },])
  const [subjectivityData, setSubjectivityData] = useState<{
    type: string;
    value: number;
}[]>([{ type: '分类一', value: 27 },])
  const [latestTwi, setLatestTwi] = useState<any[]>([])

  useEffect(() => {
    fetchTwitter()
    .then(JSONData => {
      let pdata = JSONData.filter((jd: { name: string; }) => jd.name ==='polarity')[0].details
      let sudata = JSONData.filter((jd: { name: string; }) => jd.name ==='subjectivity')[0].details
      // console.log()
      let total = 0
      Object.values(pdata).map((pd: any) => {total += pd})
      setPolarityData(Object.keys(pdata).map(pdKey => {
        return {
          type: pdKey,
          value: pdata[pdKey] / total * 100
        }
      }))
      total = 0
      Object.values(sudata).map((pd: any) => {total += pd})
      setSubjectivityData(Object.keys(sudata).map(pdKey => {
        return {
          type: pdKey,
          value: sudata[pdKey] / total * 100
        }
      }))
      setLatestTwi(JSONData.filter((jd: { name: string; }) => jd.name ==='sample')[0].details)
      // console.log()
    })
  }, [])

  useEffect(() => {
    const data = polarityData 

    const piePlot = new Pie('piePlot1', {
      appendPadding: 10,
      data,
      angleField: 'value',
      colorField: 'type',
      radius: 0.9,
      label: {
        type: 'inner',
        offset: '-30%',
        content: ({ percent }) => `${(percent * 100).toFixed(0)}%`,
        style: {
          fontSize: 14,
          textAlign: 'center',
        },
      },
      interactions: [{ type: 'element-active' }],
    });
    
    piePlot.render();
    return () => {piePlot.destroy()}
  }, [polarityData]);

  useEffect(() => {
    const data = subjectivityData
    
    const piePlot2 = new Pie('piePlot2', {
      appendPadding: 10,
      data,
      angleField: 'value',
      colorField: 'type',
      radius: 0.9,
      label: {
        type: 'inner',
        offset: '-30%',
        content: ({ percent }) => `${(percent * 100).toFixed(0)}%`,
        style: {
          fontSize: 14,
          textAlign: 'center',
        },
      },
      interactions: [{ type: 'element-active' }],
    });
    
    piePlot2.render();
    return () => {piePlot2.destroy()}
  }, [subjectivityData])

  return (
    <Stack direction='column' spacing={2}>
      <Stack direction='row' spacing={2} width='100%' justifyContent='center'>
        <div id="piePlot1"></div>
        <div id="piePlot2"></div>
      </Stack>
      <Stack direction='column' spacing={2} width='80vw'>
        <Typography variant='h4'>Sentimental analysis of latest 10 twitters</Typography>
        {latestTwi.map(lw => (
          <Card>
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                {`Subjectivity: [${lw.subjectivity}] Polarity: [${lw.polarity}] Language: [${lw.lang}]`}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {lw.text}
              </Typography>
            </CardContent>
            <CardActions>
              <Stack>
                <Typography variant="body2" color="text.secondary">
                  {`source: ${lw.source}`}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {`time: ${lw.time}`}
                </Typography>
              </Stack>
            </CardActions>
          </Card>))}
      </Stack>
    </Stack>
  )
}

export default TwitterAnalysisOptionPanel