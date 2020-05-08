'''
  @Description      
  @auther         leizi
  @create          2020-05-07 20:30
'''


def make(runcountone, runallcount, baseurl, baseport, intefacepath,
         interfacemethod, dbname, apptimename,parame):
    conect = '''<?xml version='1.0' encoding='UTF-8'?><jmeterTestPlan version='1.2' properties='5.0' jmeter='5.2.1'>
         <hashTree>
         <TestPlan guiclass='TestPlanGui' testclass='TestPlan' testname='Test Plan' enabled='true'>
         <stringProp name='TestPlan.comments'></stringProp>
         <boolProp name='TestPlan.functional_mode'>false</boolProp>
         <boolProp name='TestPlan.tearDown_on_shutdown'>true</boolProp>'\
      <boolProp name='TestPlan.serialize_threadgroups'>false</boolProp>
      <elementProp name='TestPlan.user_defined_variables' elementType='Arguments' guiclass='ArgumentsPanel' testclass='Arguments' testname='User Defined Variables' enabled='true'>
        <collectionProp name='Arguments.arguments'/>
      </elementProp>
      <stringProp name='TestPlan.user_define_classpath'></stringProp>
    </TestPlan>
    <hashTree>
      <ThreadGroup guiclass='ThreadGroupGui' testclass='ThreadGroup' testname='Thread Group' enabled='true'>
        <stringProp name='ThreadGroup.on_sample_error'>continue</stringProp>
        <elementProp name='ThreadGroup.main_controller' elementType='LoopController' guiclass='LoopControlPanel' testclass='LoopController' testname='Loop Controller' enabled='true'>
          <boolProp name='LoopController.continue_forever'>false</boolProp>
          <stringProp name='LoopController.loops'>%s</stringProp>
        </elementProp>
        <stringProp name='ThreadGroup.num_threads'>%s</stringProp>
        <stringProp name='ThreadGroup.ramp_time'>1</stringProp>
        <boolProp name='ThreadGroup.scheduler'>false</boolProp>
        <stringProp name='ThreadGroup.duration'></stringProp>
        <stringProp name='ThreadGroup.delay'></stringProp>
        <boolProp name='ThreadGroup.same_user_on_next_iteration'>true</boolProp>
      </ThreadGroup>
      <hashTree>
        <HTTPSamplerProxy guiclass='HttpTestSampleGui' testclass='HTTPSamplerProxy' testname='login' enabled='true'>
          <elementProp name='HTTPsampler.Arguments' elementType='Arguments' guiclass='HTTPArgumentsPanel' testclass='Arguments' testname='用户定义的变量' enabled='true'>
            <collectionProp name='Arguments.arguments'>%s
                </collectionProp>
          </elementProp>
          <stringProp name='HTTPSampler.domain'>%s</stringProp>
          <stringProp name='HTTPSampler.port'>%s</stringProp>
          <stringProp name='HTTPSampler.protocol'>http</stringProp>
          <stringProp name='HTTPSampler.contentEncoding'></stringProp>
          <stringProp name='HTTPSampler.path'>%s</stringProp>
          <stringProp name='HTTPSampler.method'>%s</stringProp>
          <boolProp name='HTTPSampler.follow_redirects'>true</boolProp>
          <boolProp name='HTTPSampler.auto_redirects'>false</boolProp>
          <boolProp name='HTTPSampler.use_keepalive'>true</boolProp>
          <boolProp name='HTTPSampler.DO_MULTIPART_POST'>false</boolProp>
          <stringProp name='HTTPSampler.embedded_url_re'></stringProp>
          <stringProp name='HTTPSampler.connect_timeout'></stringProp>
          <stringProp name='HTTPSampler.response_timeout'></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <ResponseAssertion guiclass='AssertionGui' testclass='ResponseAssertion' testname='Response Assertion' enabled='true'>
          <collectionProp name='Asserion.test_strings'>
            <stringProp name='67791721'>&quot;code&quot;:0</stringProp>
          </collectionProp>
          <stringProp name='Assertion.custom_message'></stringProp>
          <stringProp name='Assertion.test_field'>Assertion.response_data</stringProp>
          <boolProp name='Assertion.assume_success'>false</boolProp>
          <intProp name='Assertion.test_type'>16</intProp>
        </ResponseAssertion>
        <hashTree/>
        <DurationAssertion guiclass='DurationAssertionGui' testclass='DurationAssertion' testname='duration  assertion' enabled='true'>
          <stringProp name='DurationAssertion.duration'>200</stringProp>
        </DurationAssertion>
        <hashTree/>
        <BackendListener guiclass='BackendListenerGui' testclass='BackendListener' testname='Backend Listener' enabled='true'>
          <elementProp name='arguments' elementType='Arguments' guiclass='ArgumentsPanel' testclass='Arguments' enabled='true'>
            <collectionProp name='Arguments.arguments'>
              <elementProp name='influxdbMetricsSender' elementType='Argument'>
                <stringProp name='Argument.name'>influxdbMetricsSender</stringProp>
                <stringProp name='Argument.value'>org.apache.jmeter.visualizers.backend.influxdb.HttpMetricsSender</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='influxdbUrl' elementType='Argument'>
                <stringProp name='Argument.name'>influxdbUrl</stringProp>
                <stringProp name='Argument.value'>http://127.0.0.1:8086/write?db=%s</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='application' elementType='Argument'>
                <stringProp name='Argument.name'>application</stringProp>
                <stringProp name='Argument.value'>%s</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='measurement' elementType='Argument'>
                <stringProp name='Argument.name'>measurement</stringProp>
                <stringProp name='Argument.value'>jmeter</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='summaryOnly' elementType='Argument'>
                <stringProp name='Argument.name'>summaryOnly</stringProp>
                <stringProp name='Argument.value'>true</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='samplersRegex' elementType='Argument'>
                <stringProp name='Argument.name'>samplersRegex</stringProp>
                <stringProp name='Argument.value'>.*</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='percentiles' elementType='Argument'>
                <stringProp name='Argument.name'>percentiles</stringProp>
                <stringProp name='Argument.value'>90;95;99</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='testTitle' elementType='Argument'>
                <stringProp name='Argument.name'>testTitle</stringProp>
                <stringProp name='Argument.value'>Test name</stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
              <elementProp name='eventTags' elementType='Argument'>
                <stringProp name='Argument.name'>eventTags</stringProp>
                <stringProp name='Argument.value'></stringProp>
                <stringProp name='Argument.metadata'>=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name='classname'>org.apache.jmeter.visualizers.backend.influxdb.InfluxdbBackendListenerClient</stringProp>
        </BackendListener>
        <hashTree/>
      </hashTree>
    </hashTree>
  </hashTree>
</jmeterTestPlan>''' % (runallcount,runcountone, parame,baseurl, baseport, intefacepath, interfacemethod, dbname, apptimename)
    return conect
