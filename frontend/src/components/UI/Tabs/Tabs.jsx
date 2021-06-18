import React from 'react'
import {Tab, Tabs, TabList, TabPanel } from 'react-tabs'

const TabsUI = props => (
    <Tabs className={props.tabsClass}>
        <TabList className='TabList'>
            {props.tabs.map((tabsItem, index) => (
                <Tab className='Tab' key={index}>{tabsItem.tabHeader}</Tab>
            ))}
        </TabList>

        {
            props.tabs.map((tabsItem, index) => (
                <TabPanel className='TabPanel' key={index}>
                    <input type="text" placeholder={tabsItem.tabItem}/>
                    <button>ИСКАТЬ</button>
                </TabPanel>
            ))
        }
    </Tabs>
)

export default TabsUI