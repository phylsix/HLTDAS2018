import FWCore.ParameterSet.Config as cms

process = cms.Process('SKIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

toskim = '''/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/06AF0E29-1839-E811-A572-A4BF01011FD0.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/129C8250-FC38-E811-BBFE-EC0D9A0B3320.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/22E95B4B-F838-E811-97D2-0026181D28BB.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/38EA7F42-F838-E811-955C-5065F381E201.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/3E37DFD1-1539-E811-B920-001E675A58D9.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/4E74E5E7-1A39-E811-A99B-A4BF01013DD5.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/5C8BA4F0-0039-E811-A016-EC0D9A0B3370.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/821CE354-F238-E811-84FA-A0369F3102B6.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/9261E12D-0C39-E811-9E2F-B8CA3A70A520.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/94F41F6A-FC38-E811-AC14-24BE05C6E7E1.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/9AD897AA-1839-E811-938C-A4BF010120C5.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/9CE96747-F838-E811-82B0-B8CA3A70A520.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/A2C36999-0539-E811-BF4B-001E67DFF67C.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/BA298EC8-1539-E811-BB57-001E67A3EF70.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/D65F01EF-1A39-E811-AF43-001E67A40451.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/E06BCEF8-0039-E811-A3AB-24BE05C488E1.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/F21A9D4F-1F39-E811-8B14-5065F3818241.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/F8AE4E98-1C39-E811-8849-001E67A41EA0.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/1C1A01D3-3139-E811-9C5C-0CC47A4C8E86.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/6E712531-3339-E811-AA9C-0CC47A4D767E.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/76A4652D-2F39-E811-B162-003048FFD75A.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/7A69B59D-2839-E811-831A-0CC47A78A3F4.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/90C53C52-F838-E811-A3AE-003048FFD7AA.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/986B1FB4-0539-E811-8E62-E0071B6C9DA0.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/A23ED157-2839-E811-933E-0CC47A78A408.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/B8D19224-1939-E811-95A8-24BE05C6D5A1.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/BC427B74-F838-E811-A987-4C79BA181247.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/CEA54C8F-2839-E811-AB8B-0CC47A4D7690.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/D6A05275-0239-E811-96D8-0CC47A4D7632.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/DEF9FB8D-FD38-E811-8BB7-0CC47A4D765E.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/EC4F831D-2839-E811-BF17-0025905A48C0.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/80000/F6AE9346-FE38-E811-9BEE-E0071B740D90.root
/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/90000/6E23BB6D-F538-E811-9EEE-E0071B7A58B0.root'''
# Input source
process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
       #'/store/data/Run2016G/SingleElectron/MINIAOD/23Sep2016-v1/100000/004A7893-A990-E611-B29F-002590E7DE36.root',
       #'/store/data/Run2017F/SingleElectron/MINIAOD/31Mar2018-v1/30000/24B1B0A9-DA38-E811-A292-0CC47A4C8E66.root',
       #'/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/06300247-1239-E811-A8C5-A4BF01027688.root',
       toskim.split('\n')
   ),
)


process.options = cms.untracked.PSet(
    numberOfThreads=cms.untracked.uint32(8)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('RelVal nevts:100'),
    name = cms.untracked.string('Applications')
)

# JSON

import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt').getVLuminosityBlockRange()

# skim definitions

process.highpfmet = cms.EDFilter("PtMinCandViewSelector",
                           src = cms.InputTag("slimmedMETs"),
                           ptMin = cms.double(150)
)

process.metFilter = cms.EDFilter("CandViewCountFilter",
  src = cms.InputTag("highpfmet"),
  minNumber = cms.uint32(1),
)

process.pfmet_filter_step = cms.Path(process.highpfmet + process.metFilter)


# Output definition

process.Out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string ("skim_pfmet150_Run2017D_SingleElectron.root"),
                               outputCommands = cms.untracked.vstring('keep *'),
                               SelectEvents = cms.untracked.PSet(
                                   SelectEvents = cms.vstring('pfmet_filter_step')
                               ),
)
  
#process.GlobalTag.globaltag = "80X_dataRun2_2016SeptRepro_v3"
process.GlobalTag.globaltag = "94X_dataRun2_ReReco_EOY17_v6"

# Path and EndPath definitions
process.output_step = cms.EndPath(process.Out)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
