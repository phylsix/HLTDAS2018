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
    input = cms.untracked.int32(-1)
)

toskim = '''/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/9A4FE434-1C38-E811-847D-001E67E68BBD.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/7836E9BE-2D37-E811-AA01-001E67A40442.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/382875DA-2937-E811-9E7E-001E675A68BF.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/3288BA97-2737-E811-B5CF-001E675A6630.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/F8E965EE-2537-E811-889B-001517FB2250.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/3ABB031E-2237-E811-8B84-001E67DFF735.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/B48C7BDD-1C37-E811-8578-001E67A39C17.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/6AD0B4FF-1737-E811-8509-001E67A3FE66.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/526D3BF5-0C37-E811-AEE6-001E675A58D9.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/58CB28BD-0237-E811-A6F1-001E67A40523.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/22D3B3F8-FB36-E811-9390-001E67E5A39A.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/068104AF-F436-E811-A4FA-A4BF010255AE.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/5496796C-F036-E811-8CB0-001E67A42026.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/BC8B95A3-2538-E811-87CC-0CC47AA478BE.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/46B7581F-AF37-E811-8056-0CC47A0AD74E.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30003/249A4C96-6F37-E811-AD99-0CC47A0AD6C4.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30001/46D9F883-6F37-E811-A69B-0CC47AA53D98.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30001/34F35A8F-4A37-E811-8296-00259075D72E.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30001/08136474-4A37-E811-AEE8-002590D9D8B6.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30001/AE8BF154-4A37-E811-8034-002590FD5694.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/18A0AC24-8C37-E811-A75C-002590FD5A3A.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30003/8487230B-4A37-E811-9F85-0CC47A0AD6C4.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/B2D15ABC-8437-E811-BCB6-0CC47AA53D68.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/1CC915E9-7C37-E811-90AF-0CC47AA53D82.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/9CEBD3F4-7437-E811-AAEB-0CC47AA4861C.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/787DF5E9-7237-E811-B7A9-0CC47A57CB8E.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30001/02F626CB-2B37-E811-A990-0CC47AA53D6A.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/C025E5DE-7037-E811-825C-0025907859B8.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/8419E237-6D37-E811-8DFC-0CC47AA53D76.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/2E4CD795-6A37-E811-B0BC-0CC47A57D086.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/540028A6-6637-E811-AE3F-0CC47A57D086.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/FC1465B1-6637-E811-B261-0CC47AA53D98.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/6E31CF16-5437-E811-8692-0CC47A57CE00.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/DAD67C8A-4437-E811-A453-0CC47AA53D58.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/B6F0704F-4037-E811-88A4-002590D9D880.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/5A3D42EF-3837-E811-99D8-0CC47A0AD48A.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/CA1FEBE1-2C37-E811-A9CE-00259075D702.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/D6E4FACA-1C37-E811-BCD9-0CC47A57CCF4.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/50060DA4-1837-E811-A683-0CC47A0AD74E.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/46B6DCCD-1437-E811-823D-0CC47AA53D72.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/1A707A9D-0A37-E811-BC9F-0CC47A57CC42.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/8E75FAB3-0437-E811-ACE0-003048CB860C.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/1862C080-F136-E811-B566-0025901F8740.root
/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/30000/20234DAB-E936-E811-9DF4-002590FD5A3A.root'''

# Input source
process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
       #'/store/data/Run2017F/SingleMuon/MINIAOD/31Mar2018-v1/00000/7836E9BE-2D37-E811-AA01-001E67A40442.root',
       toskim.split('\n')
   ),
)


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('RelVal nevts:100'),
    name = cms.untracked.string('Applications')
)

# JSON

import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_MuonPhys.txt').getVLuminosityBlockRange()

# skim definitions

process.highptMuons = cms.EDFilter("PtMinCandViewSelector",
                           src = cms.InputTag("slimmedMuons"),
                           ptMin = cms.double(20)
)

process.dimuonFilter = cms.EDFilter("CandViewCountFilter",
  src = cms.InputTag("highptMuons"),
  minNumber = cms.uint32(2),
)

process.dimu_filter_step = cms.Path(process.highptMuons + process.dimuonFilter)


# Output definition

process.Out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string ("skim_dimu20_Run2017F_SingleMuon_ReReco.root"),
                               outputCommands = cms.untracked.vstring('keep *'),
                               SelectEvents = cms.untracked.PSet(
                                   SelectEvents = cms.vstring('dimu_filter_step')
                               ),
)
  
process.GlobalTag.globaltag = "94X_dataRun2_ReReco_EOY17_v6"

# Path and EndPath definitions
process.output_step = cms.EndPath(process.Out)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
