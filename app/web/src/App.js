// SPDX-FileCopyrightText: 2020 Robert Cohn
//
// SPDX-License-Identifier: MIT

import React from 'react';
import {
    VictoryAxis,
    VictoryBrushContainer,
    VictoryChart,
    VictoryLine,
    VictoryZoomContainer,
} from 'victory';

import './App.css';

class StripChart extends React.Component {
    constructor() {
        super();
        this.state = {};
    }

    handleZoom(domain) {
        this.setState({selectedDomain: domain});
    }

    handleBrush(domain) {
        this.setState({zoomDomain: domain});
    }

    render() {
        return (
            <div>
              <VictoryChart
                width={550}
                height={300}
                scale={{x: "time"}}
                containerComponent={
                    <VictoryZoomContainer
                      responsive={false}
                      zoomDimension="x"
                      zoomDomain={this.state.zoomDomain}
                      onZoomDomainChange={this.handleZoom.bind(this)}
                    />
                }
              >
                <VictoryLine
                  style={{
                      data: {stroke: "tomato"}
                  }}
                  data={[
                      {x: new Date(1982, 1, 1), y: 125},
                      {x: new Date(1987, 1, 1), y: 257},
                      {x: new Date(1993, 1, 1), y: 345},
                      {x: new Date(1997, 1, 1), y: 515},
                      {x: new Date(2001, 1, 1), y: 132},
                      {x: new Date(2005, 1, 1), y: 305},
                      {x: new Date(2011, 1, 1), y: 270},
                      {x: new Date(2015, 1, 1), y: 470}
                  ]}
                />

              </VictoryChart>

              <VictoryChart
                width={550}
                height={90}
                scale={{x: "time"}}
                padding={{top: 0, left: 50, right: 50, bottom: 30}}
                containerComponent={
                    <VictoryBrushContainer responsive={false}
                                           brushDimension="x"
                                           brushDomain={this.state.selectedDomain}
                                           onBrushDomainChange={this.handleBrush.bind(this)}
                    />
                }
              >
                <VictoryAxis
                  tickValues={[
                      new Date(1985, 1, 1),
                      new Date(1990, 1, 1),
                      new Date(1995, 1, 1),
                      new Date(2000, 1, 1),
                      new Date(2005, 1, 1),
                      new Date(2010, 1, 1),
                      new Date(2015, 1, 1)
                  ]}
                  tickFormat={(x) => new Date(x).getFullYear()}
                />
                <VictoryLine
                  style={{
                      data: {stroke: "tomato"}
                  }}
                  data={[
                      {x: new Date(1982, 1, 1), y: 125},
                      {x: new Date(1987, 1, 1), y: 257},
                      {x: new Date(1993, 1, 1), y: 345},
                      {x: new Date(1997, 1, 1), y: 515},
                      {x: new Date(2001, 1, 1), y: 132},
                      {x: new Date(2005, 1, 1), y: 305},
                      {x: new Date(2011, 1, 1), y: 270},
                      {x: new Date(2015, 1, 1), y: 470}
                  ]}
                />
              </VictoryChart>
            </div>
        );
    }
}



function Led(props) {
    return (
      <div> {props.name} : {props.on ? 'On' : 'Off' } </div>
    );
}

class LedMatrix extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            led_on: Array(9).fill(false),
            led_name: props.names
        }
    }
    renderLed(index) {
        return (
                <Led
                  name={this.state.led_name[index]}
                  on={this.state.led_on[index]}
                />
        );
    }
    render() {
        return (
                <>
                  <div>
                    {this.renderLed(0)}
                    {this.renderLed(1)}
                    {this.renderLed(2)}
                 </div>
                 <div>
                    {this.renderLed(3)}
                    {this.renderLed(4)}
                    {this.renderLed(5)}
                 </div>
               </>
        );
    }
}

class ControlPanel extends React.Component {
    constructor(props) {
        super(props);
        this.led_names = [
            '1st Floor',
            '2nd Floor',
            'Water Heater',
            'Oil Burner',
            'Unused',
            'Unused'
        ]
    }
    render() {
        return (
                <>
                  <h1> Sensepy Control Panel </h1>
                  <LedMatrix
                    names={this.led_names}
                  />
                  <StripChart />
                </>
        )
    }
}


function App() {
  return (
    <ControlPanel />
  );
}

export default App;
