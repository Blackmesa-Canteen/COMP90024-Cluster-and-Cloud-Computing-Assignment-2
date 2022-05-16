import React, { useContext, useEffect, useState } from "react";
import { DataDisplayContext } from "../../App";
import { Chart } from '@antv/g2';

interface Top10LanguageAnalysisPanelProps {
  languageCountData: any[]
}

const Top10LanguageAnalysisPanel = ({ languageCountData }: Top10LanguageAnalysisPanelProps) => {
  const { displayOptions } = useContext(DataDisplayContext)
  const [displayData, setDisplayData] = useState<any[]>([])

  useEffect(() => {
    let resultData: {[index: string]: number} = {}
    languageCountData.filter(ld => (ld.date >= displayOptions[0] && ld.date <= displayOptions[1]))
    .map(ld => {
      Object.keys(ld.languageCount).map(language => {
        if (resultData[language as string]) {
          resultData[language] += ld.languageCount[language]
        }
        else {
          resultData = {
            ...resultData,
            [language]: ld.languageCount[language]
          }
        }
      })
    })
    const d = Object.keys(resultData).map(keyd => {
      return {
        xValue: keyd,
        yValue: resultData[keyd]
      }
    }).sort((a, b) => {
      if (a.yValue > b.yValue) {
        return -1
      }
      else if(a.yValue < b.yValue) {
        return 1
      }
      return 0
    })
    setDisplayData(d.slice(0, 11))
  }, 
  [displayOptions, languageCountData])

  useEffect(() => {
    const chart = new Chart({
      container: 'container',
      autoFit: true,
      height: 500,
      padding: [50, 20, 50, 20],
    });
    chart.data(displayData);
    chart.scale('yValue', {
      alias: 'Count',
    });
    
    chart.axis('xValue', {
      tickLine: {
        alignTick: false,
      },
    });
    chart.axis('yValue', false);
    
    chart.tooltip({
      showMarkers: false,
    });
    chart.interval().position('xValue*yValue');
    chart.interaction('element-active');
    
    
    chart.render();

    return () => {
      chart.destroy()
    }
  }, [displayData])

  return (
    <div id='container' style={{minWidth: '80vw', minHeight: '70vh'}}></div>
  )
}

export default Top10LanguageAnalysisPanel