import FWCore.ParameterSet.Config as cms

process = cms.Process('HLTANALYZER')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:skim_dimu20_Run2017F_SingleMuon_ReReco.root'),
   #fileNames = cms.untracked.vstring('/store/user/cmsdas/2017/short_exercises/Trigger/skim_dimu20_SingleMuon_2016G_ReReco_180k.root'), # skimmed file on EOS at LPC
)


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('RelVal nevts:100'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histos_SingleMuTrigAnalyzer.root')
                                   )

### analyzer configuration

process.singleMuTrigAnalyzerMiniAOD = cms.EDAnalyzer("SingleMuTrigAnalyzerMiniAOD")
process.singleMuTrigAnalyzerMiniAOD.triggerName = cms.untracked.string("HLT_IsoMu24_v10")
process.singleMuTrigAnalyzerMiniAOD.verbose = cms.untracked.bool(False)

process.GlobalTag.globaltag = "94X_dataRun2_ReReco_EOY17_v6"

# Path and EndPath definitions
process.HLTanalyzers = cms.Path(process.singleMuTrigAnalyzerMiniAOD)
